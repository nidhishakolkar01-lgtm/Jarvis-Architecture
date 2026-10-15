"""
JARVIS-Sentinel: Dynamic Execution Graph Rollback Engine
Reference implementation demonstrating transactional state checkpointing and rollback routines.
"""

import hashlib
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class StateSnapshot:
    """Represents a discrete verified state vector."""
    snapshot_id: str
    state_hash: str
    data: Dict
    timestamp: float = field(default_factory=time.time)


class RollbackTriggeredException(Exception):
    """Raised when state drift triggers an automated rollback."""
    pass


class SentinelRollbackEngine:
    """Manages transactional state checkpoints and executes sub-second rollbacks."""

    def __init__(self, drift_threshold: float = 0.25):
        self.drift_threshold = drift_threshold
        self._history: List[StateSnapshot] = []
        self._current_state: Dict = {}
        # Initialize root checkpoint
        self.create_checkpoint({"_root": True, "init_timestamp": time.time()})

    def create_checkpoint(self, state_data: Dict) -> StateSnapshot:
        """Computes monotonic hash and creates a recoverable state checkpoint."""
        serialized = str(sorted(state_data.items())).encode("utf-8")
        state_hash = hashlib.sha256(serialized).hexdigest()
        
        snapshot = StateSnapshot(
            snapshot_id=f"snap_{len(self._history) + 1}",
            state_hash=state_hash,
            data=dict(state_data),
        )
        self._history.append(snapshot)
        self._current_state = dict(state_data)
        return snapshot

    def verify_transaction(self, candidate_state: Dict, drift_score: float) -> bool:
        """Evaluates drift score and either commits or executes a sub-second rollback.
        
        Args:
            candidate_state: State vector proposed by worker subagent.
            drift_score: Normalized divergence score [0.0 - 1.0].
            
        Returns:
            True if committed successfully.
            
        Raises:
            RollbackTriggeredException: If drift score exceeds safety threshold.
        """
        if drift_score > self.drift_threshold:
            self.execute_rollback(reason=f"Drift score {drift_score:.2f} exceeded threshold {self.drift_threshold}")
            raise RollbackTriggeredException(f"State mutation rejected; rolled back to {self.get_latest_checkpoint().snapshot_id}")

        self.create_checkpoint(candidate_state)
        return True

    def execute_rollback(self, reason: str) -> StateSnapshot:
        """Restores state to the most recent verified checkpoint."""
        if len(self._history) <= 1:
            # Revert to root
            self._current_state = dict(self._history[0].data)
            return self._history[0]

        # Revert to previous valid checkpoint
        latest_valid = self._history[-1]
        self._current_state = dict(latest_valid.data)
        return latest_valid

    def get_latest_checkpoint(self) -> StateSnapshot:
        return self._history[-1]

    @property
    def current_state(self) -> Dict:
        return dict(self._current_state)

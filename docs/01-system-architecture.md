# JARVIS System Architecture & Orchestration Specification

## 1. Overview & Architectural Principles

JARVIS operates on an **event-driven, hierarchical supervisor-worker model** designed for autonomous execution over long-horizon developer workflows.

Traditional single-agent loops suffer from token-context exhaustion, uncontrolled hallucination cascades, and irreversible workspace mutations. JARVIS decouples execution into four orthogonal layers:

1. **Strategic Planning Layer (Supervisor):** Decomposes ambiguous human intent into structured Directed Acyclic Graphs (DAGs).
2. **Deterministic Execution Layer (Worker Nodes):** Executes isolated unit tasks under strict AST and static analysis boundaries.
3. **Observability & Liveness Layer (Heartbeat Loop):** Continuous WebSocket telemetry streaming for workspace state monitoring.
4. **State Consistency Layer (Sentinel Engine):** Checkpoint validation with sub-second state rollback triggers.

---

## 2. Supervisor-Worker Topology

```
+-------------------------------------------------------------+
|                      Supervisor Agent                       |
|  - Goal Ingestion & Semantic Disambiguation                 |
|  - Dynamic Subagent Provisioning & Lifecycle Management     |
|  - Shared Memory & Monotonic State Aggregation              |
+-------------------------------------------------------------+
                               |
            +------------------+------------------+
            |                                     |
            v                                     v
+-----------------------+             +-----------------------+
|  Worker Subagent A    |             |  Worker Subagent B    |
|  - Code Generation    |             |  - Testing & Lint     |
|  - AST Validation     |             |  - Docker Sandbox     |
+-----------------------+             +-----------------------+
```

### 2.1 Dynamic DAG Decomposition
The supervisor parses high-level objectives into tasks represented as nodes in a DAG:
$$G = (V, E)$$
Where:
* $V = \{v_1, v_2, \dots, v_n\}$ represents atomic tasks (e.g., file creation, test execution, schema migration).
* $E = \{(v_i, v_j) \mid v_i \text{ must strictly precede } v_j\}$ defines deterministic dependency constraints.

Independent nodes ($v_a, v_b \text{ where } (v_a, v_b) \notin E \text{ and } (v_b, v_a) \notin E$) are executed in parallel across isolated subagent containers.

---

## 3. Multi-Layer Validation Gates

Before any generated code is executed in an environment, it must pass through **three synchronous validation gates**:

1. **Gate 1: Static AST Parsing (`ast.parse`)**
   - Verifies syntactical correctness.
   - Forbids blacklisted calls (e.g., unauthorized `os.system('rm -rf')`, raw socket binds, or destructive environment alterations) unless explicitly sandboxed.
2. **Gate 2: Type & Contract Enforcement**
   - In TypeScript/Python, interfaces are checked against formal schemas before payload consumption.
3. **Gate 3: Containerized Dry-Run Sandbox**
   - Executes unit tests within an isolated ephemeral Docker container with read-only root filesystems and bounded memory limits (cgroups).

---

## 4. State Synchronization & Monotonic Memory

In distributed agent workflows, shared memory corruption (*state drift*) occurs when concurrent workers read stale state. JARVIS implements **Monotonic Version Checkpointing**:
* Every state transition creates a cryptographically hashed state vector:
  $$S_{t+1} = \text{SHA256}(S_t \mathbin{\Vert} \Delta_{\text{worker}})$$
* A worker cannot commit $\Delta$ if its base state $S_{\text{base}} \neq S_{\text{current}}$, preventing race conditions across parallel branches.

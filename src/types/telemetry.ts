/**
 * JARVIS Proactive Telemetry & Heartbeat Types
 * Defines structural contracts for workspace liveness, anomaly detection, and state synchronization.
 */

export type AgentExecutionStatus = 
  | 'INITIALIZING'
  | 'HEALTHY'
  | 'DRIFT_SUSPECTED'
  | 'ANOMALY_DETECTED'
  | 'ROLLBACK_IN_PROGRESS'
  | 'TERMINATED';

export type InterventionType = 
  | 'AUTO_LINT'
  | 'GENERATE_TESTS'
  | 'OPTIMIZE_CONTEXT'
  | 'TRIGGER_ROLLBACK'
  | 'ALERT_SUPERVISOR';

export interface WorkspaceMetrics {
  rootPath: string;
  activeFilePath?: string;
  dirtyFileCount: number;
  lastEditTimestamp: number;
  gitBranch: string;
  isStalled: boolean;
}

export interface ResourceTelemetry {
  cpuUsagePct: number;
  memoryAllocatedMb: number;
  activeGoroutinesOrPromises: number;
  driftScore: number; // 0.00 (deterministic) to 1.00 (severe drift)
}

export interface HeartbeatTelemetryFrame {
  frameId: string;
  timestamp: number;
  agentId: string;
  status: AgentExecutionStatus;
  workspace: WorkspaceMetrics;
  metrics: ResourceTelemetry;
  suggestedIntervention?: InterventionType;
}

export interface StateTransactionRecord {
  transactionId: string;
  agentId: string;
  action: string;
  resourceUri: string;
  previousStateHash: string;
  newStateHash: string;
  timestamp: number;
  verified: boolean;
}

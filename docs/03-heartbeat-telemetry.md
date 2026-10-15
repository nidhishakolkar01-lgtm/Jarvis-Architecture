# Proactive Heartbeat Loop & Workspace Telemetry Protocol

## 1. Motivation: Proactive vs Reactive Autonomous Agents

Most developer agents operate **reactively**: they wait silently until the developer types a prompt. 

JARVIS implements **proactive telemetry loops** in TypeScript:
* Rather than remaining idle, a background supervisor agent actively monitors workspace telemetry (file edits, test outputs, compiler warnings, terminal activity).
* It detects developer fatigue, context switching, or build stalls and proactively suggests or executes targeted background tasks (e.g., auto-generating unit tests for newly written modules, running linter checks, or warming up build caches).

---

## 2. Heartbeat Event Lifecycle

```
[Interval Timer (e.g. 5000ms)]
              │
              ▼
    [Collect Workspace Metrics]
              │
              ├──> Git Working Directory Status
              ├──> Active Buffer Diff Size
              ├──> Process Liveness / CPU Load
              └──> Inactive Duration
              │
              ▼
   [Telemetry Frame Packaging]
              │
              ▼
  [Stream via WebSocket to Agent Hub]
              │
     ┌────────┴────────┐
     ▼                 ▼
[Normal State]   [Threshold Breach]
(No-op / Log)    (Trigger Proactive Intervention)
```

---

## 3. Telemetry Frame Specification

Every heartbeat event emits a validated JSON payload conforming to the TypeScript schema defined in `src/types/telemetry.ts`:

```json
{
  "frameId": "frame_9a8f2c",
  "timestamp": 1729000000000,
  "agentId": "agent_worker_42",
  "workspace": {
    "rootPath": "/workspace/project",
    "dirtyFileCount": 3,
    "lastEditTimestamp": 1729000000000
  },
  "metrics": {
    "cpuUsagePct": 14.2,
    "memoryAllocatedMb": 256.4,
    "driftScore": 0.02
  },
  "status": "HEALTHY"
}
```

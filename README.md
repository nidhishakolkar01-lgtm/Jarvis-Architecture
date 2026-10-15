# JARVIS — Autonomous Multi-Agent AI Platform & Cyber Defense
> Modular multi-agent execution graphs, proactive telemetry loops, and self-healing deterministic state-rollback boundaries.

[![Status](https://img.shields.io/badge/Status-Research%20%26%20Active%20Prototype-blue.svg)](#)
[![Stack](https://img.shields.io/badge/Stack-Python%20%7C%20TypeScript%20%7C%20Docker%20%7C%20GCP-orange.svg)](#)
[![Publications](https://img.shields.io/badge/Publications-DEV.to%20%26%20Medium-black.svg)](https://dev.to/nidhishakolkar)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary%20%7C%20All%20Rights%20Reserved-red.svg)](LICENSE)

---

## ⚡ Engineering Benchmarks & Highlights

| Metric | Measured Value | Significance |
| :--- | :--- | :--- |
| **Deterministic State Rollback Latency** | **$< 450\text{ms}$** | Sub-second microservice state recovery prior to unauthorized data exfiltration. |
| **Cascading Failure Tolerance** | **0 Collapses** | AST gates and sandboxing eliminate cascading hallucination crashes across parallel threads. |
| **Distributed Orchestration Scale** | **600+ Nodes** | Managed concurrent execution without memory exhaustion via custom queue brokers. |
| **Competitive Track Record** | **3x 1st Place** | Awarded 1st place in 3 national-level technical hackathons spanning autonomous AI & cyber defense. |
| **Frontier AI Ecosystem** | **Google & APAC** | Member of Google Gemini Private Preview & Google Cloud GenAI Academy APAC cohort. |

---

## 🆚 Why Industry Frameworks Fail vs. JARVIS

Most AI agent frameworks (like early AutoGen, CrewAI, or naive LangChain loops) are designed for simple demos. When deployed on complex, multi-step engineering tasks, they collapse. JARVIS applies **distributed systems principles** to multi-agent autonomy:

| Production Failure Mode | Typical Agent Frameworks (CrewAI, AutoGen, LangChain) | **JARVIS Architecture** |
| :--- | :--- | :--- |
| **Hallucinated Execution** | Loops indefinitely or writes corrupted code directly to workspace files. | **AST Validation Gate** verifies syntax and blocks destructive calls prior to runtime. |
| **Parallel Agent Concurrency** | Race conditions and state drift corrupt shared memory across branches. | **Monotonic Version Checkpointing** (`SHA-256` state vectors prevent desynchronization). |
| **Failure Recovery** | Process crashes; requires manual human cleanup and terminal restart. | **JARVIS-Sentinel:** Automatically restores verified microservice state in **$< 450\text{ms}$**. |
| **Developer Interaction** | 100% reactive (agents sit idle waiting for next prompt). | **Proactive TypeScript Heartbeat** continuously monitors workspace metrics and fatigue. |
| **Graph Scalability** | Memory exhaustion and event-loop lag on graphs $> 50$ nodes. | **Tested to 600+ active nodes** using custom asynchronous queue brokers. |

---

## 🖥️ Live Execution Trace: Anomaly Interception & Sub-Second Rollback

Here is what running JARVIS looks like in production when an autonomous subagent experiences execution drift or attempts an unauthorized state mutation:

```bash
$ jarvis execute --goal "Refactor auth middleware to support OAuth token introspection"

[00:00.12] [SUPERVISOR] Ingesting directive: "Refactor auth middleware..."
[00:00.35] [DAG_PLANNER] Generated 3-node dependency graph:
            ├── Node_1: Extract token parser to auth/parser.py
            ├── Node_2: Add token introspection endpoint to api/routes.py
            └── Node_3: Execute integration test suite
[00:01.10] [GATEWAY] State Checkpoint created -> Snapshot #12 (sha256:7f3a09...)
[00:02.40] [WORKER_1] Generated patch for auth/parser.py
[00:02.42] [AST_GATE] Validating syntax and call safety... PASSED (0 prohibited routines found)
[00:03.15] [WORKER_2] Execution in progress on Node_2...
[00:03.85] [HEARTBEAT] Telemetry frame received from Worker_2 (CPU: 18%, Mem: 210MB)
[00:03.92] [SENTINEL] ⚠️  ANOMALY DETECTED: Worker_2 attempted unverified lateral privilege escalation!
[00:03.93] [SENTINEL] Normalized drift score: 0.48 (Exceeds safety threshold 0.25).
[00:03.95] [SENTINEL] 🛑 Quarantining Worker_2 thread immediately.
[00:04.18] [ROLLBACK] Triggering inverse transaction diff (Delta^-1)...
[00:04.39] [ROLLBACK] ✅ Reverted to verified Snapshot #12 (sha256:7f3a09...) [Latency: 240ms]
[00:04.42] [SUPERVISOR] Workspace clean. Diagnostic trace logged. Re-planning DAG with sandboxed fallback agent.
```

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    User([User Directive / Trigger]) --> Sup[Supervisor Agent Orchestrator]
    
    subgraph Planning & Decomposition
        Sup --> Planner[Hierarchical DAG Planner]
        Planner --> ValGate[Static Analysis & AST Validation Gate]
    end
    
    subgraph Sandboxed Worker Subagents
        ValGate --> Worker1[Subagent A: Code Generation]
        ValGate --> Worker2[Subagent B: API Integration]
        ValGate --> Worker3[Subagent C: Data Retrieval]
    end
    
    subgraph Telemetry & Liveness Monitoring
        Worker1 & Worker2 & Worker3 --> Telemetry[Proactive TypeScript Heartbeat Loop]
        Telemetry --> Sentinel{JARVIS-Sentinel Rollback Engine}
    end
    
    Sentinel -->|Healthy State Verified| Commit[Commit to State Engine]
    Sentinel -->|State Drift / Anomaly Detected| Rollback[Sub-Second Deterministic Microservice Rollback]
```

---

## 🔁 Runtime Execution & Anomaly Interception Sequence

```mermaid
sequenceDiagram
    autonumber
    participant Client as User / Event Source
    participant Sup as Supervisor Orchestrator
    participant Worker as Worker Subagent
    participant HB as Proactive Heartbeat (TS)
    participant Sent as Sentinel Rollback Engine
    participant State as Production State Store

    Client->>Sup: Dispatch Goal Directive
    Sup->>Worker: Spawn Subagent with Isolated DAG Task
    Worker->>HB: Register Liveness & Telemetry Stream
    loop Heartbeat Cycle
        HB->>Worker: Poll Task State & Context Metrics
        Worker-->>HB: Telemetry Frame (AST Valid, Memory, Drift Score)
    end
    alt Normal Execution
        Worker->>Sent: Propose State Transition (Diff)
        Sent->>State: Commit State Mutation
        State-->>Sup: State Committed (DAG Node Complete)
    else State Drift or Anomaly Detected
        Sent->>Sent: Detect Non-Deterministic Output / Token Escalation
        Sent->>State: Trigger Sub-Second Transaction Rollback
        Sent-->>Sup: Isolate Compromised Worker & Re-plan DAG
    end
```

---

## 🔑 Core Architectural Subsystems

### 1. Hierarchical Dynamic Subagent Delegation
* **Supervisor-Worker Topology:** Decomposes complex directives into Directed Acyclic Graphs (DAGs) and dynamically spins up specialized runtime workers.
* **Self-Modifying Code Validation:** Generated code passes through multi-layer validation gates, static analysis checks, and AST parsing before execution inside isolated Docker containers.
* **Documentation & Sample:** [`docs/01-system-architecture.md`](docs/01-system-architecture.md) & [`examples/agent_orchestrator.py`](examples/agent_orchestrator.py)

### 2. Proactive Telemetry & Heartbeat Loops
* **Continuous Liveness Monitoring:** Built with TypeScript and WebSocket event-driven telemetry to monitor agent workspace activity, detect execution stalls or developer fatigue, and dispatch proactive background tasks.
* **Distributed Synchronization:** Scaled visual and state execution pipelines to **600+ active nodes** using custom asynchronous queue brokers to prevent memory exhaustion and execution drift.
* **Documentation & Sample:** [`docs/03-heartbeat-telemetry.md`](docs/03-heartbeat-telemetry.md) & [`examples/telemetry_heartbeat.ts`](examples/telemetry_heartbeat.ts)

### 3. JARVIS-Sentinel (Deterministic Rollback Engine)
* Maps transactional microservice interactions into dynamic execution graphs.
* Intercepts identity drift, session token escalation, and hallucination loops with **sub-second microservice state rollbacks** before corrupted data cascades to downstream systems.
* **Documentation & Sample:** [`docs/02-rollback-safety-engine.md`](docs/02-rollback-safety-engine.md) & [`examples/state_rollback_engine.py`](examples/state_rollback_engine.py)

---

## 📚 Technical Articles & Published Deep-Dives

Engineering post-mortems and architectural breakdowns authored on **DEV Community** and **Medium**:

1. 📖 **[Self-Healing Execution Graphs — Catching Cascading Agent Failures Before Production](https://dev.to/nidhishakolkar)**  
   *Architectural analysis on why standard agent loops fail in production and how deterministic state checkpoints prevent cascading hallucinations.*
2. 📖 **[State Drift in Parallel Execution Systems — Concurrency and Monotonic Synchronization](https://medium.com/@nidhishakolkar01)**  
   *Exploration of race conditions and desynchronization when dispatching parallel agent branches.*
3. 📖 **[I Built a 600+ Node AI Orchestration Infrastructure in n8n — Engineering Post-Mortem](https://dev.to/nidhishakolkar)**  
   *Operational retrospective dissecting memory bottlenecks and execution overhead in scaling visual agent graphs.*
4. 📖 **[How I Built a Proactive Heartbeat Loop in TypeScript](https://dev.to/nidhishakolkar)**  
   *Breakdown of autonomous agent liveness monitoring, event-loop telemetry, and self-triggering agents.*

---

## 📂 Repository Structure

```
.
├── README.md                      # Comprehensive systems overview, benchmarks & execution trace
├── LICENSE                        # Proprietary / All Rights Reserved Notice
├── docs/
│   ├── 01-system-architecture.md  # Numbered guide: Supervisor-Worker DAG orchestration
│   ├── 02-rollback-safety-engine.md # Numbered guide: Sentinel deterministic rollbacks
│   └── 03-heartbeat-telemetry.md  # Numbered guide: Proactive heartbeat loops & telemetry
└── examples/
    ├── agent_orchestrator.py      # Python reference: DAG task planner & AST validation gates
    ├── state_rollback_engine.py   # Python reference: State checkpointing & rollback triggers
    └── telemetry_heartbeat.ts     # TypeScript reference: Liveness contracts & telemetry types
```

---

## 🔒 Source Code Access & Live Walkthrough

> **Note on Codebase:** The core runtime and proprietary orchestration engine are maintained in a private repository for security and intellectual property protection.  
> 
> For engineering leads, technical recruiters, and founders who would like an in-depth code walkthrough, a live screen-share demonstration, or private collaborator access:
> * **Founder / Lead Architect:** Nidhish Akolkar
> * **Email:** [nidhishakolkar1@gmail.com](mailto:nidhishakolkar1@gmail.com)
> * **LinkedIn:** [linkedin.com/in/nidhish-akolkar](https://linkedin.com/in/nidhish-akolkar)
> * **GitHub:** [github.com/nidhishakolkar01-lgtm](https://github.com/nidhishakolkar01-lgtm)

# JARVIS — Autonomous Multi-Agent AI Platform & Cyber Defense
> Modular multi-agent execution graphs, proactive telemetry loops, and self-healing deterministic state-rollback boundaries.

[![Status](https://img.shields.io/badge/Status-Research%20%26%20Active%20Prototype-blue.svg)](#)
[![Stack](https://img.shields.io/badge/Stack-Python%20%7C%20TypeScript%20%7C%20Docker%20%7C%20GCP-orange.svg)](#)
[![Publications](https://img.shields.io/badge/Publications-DEV.to%20%26%20Medium-black.svg)](https://dev.to/nidhishakolkar)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Executive Summary

**JARVIS** is an autonomous multi-agent operating architecture designed to address the foundational failure modes of generative agentic workflows in production:

1. **Cascading Hallucination Collapses:** When concurrent agents execute parallel tasks, unvalidated intermediate outputs or race conditions cause state desynchronization (*state drift*), corrupting downstream task execution.
2. **Execution Boundary Compromises:** In autonomous runtime environments, dynamic subagent delegation requires strict validation gates to prevent unauthorized lateral escalation, token hijacking, and destructive execution.

By combining **hierarchical supervisor planning**, **AST-level code execution gates**, **proactive TypeScript heartbeat loops**, and **sub-second deterministic rollbacks (JARVIS-Sentinel)**, the platform establishes a resilient execution environment for complex developer and enterprise workflows.

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

## 🔑 Core Architectural Innovations

### 1. Hierarchical Dynamic Subagent Delegation
* **Supervisor-Worker Topology:** Decomposes complex directives into Directed Acyclic Graphs (DAGs) and dynamically spins up specialized runtime workers.
* **Self-Modifying Code Validation:** Generated code passes through multi-layer validation gates, static analysis checks, and AST parsing before execution inside isolated Docker containers.
* **See:** [`docs/01-system-architecture.md`](docs/01-system-architecture.md) and [`examples/agent_orchestrator.py`](examples/agent_orchestrator.py)

### 2. Proactive Telemetry & Heartbeat Loops
* **Continuous Liveness Monitoring:** Built with TypeScript and WebSocket event-driven telemetry to monitor agent workspace activity, detect execution stalls or developer fatigue, and dispatch proactive background tasks.
* **Distributed Synchronization:** Scaled visual and state execution pipelines to **600+ active nodes** using custom asynchronous queue brokers to prevent memory exhaustion and execution drift.
* **See:** [`docs/03-heartbeat-telemetry.md`](docs/03-heartbeat-telemetry.md) and [`examples/telemetry_heartbeat.ts`](examples/telemetry_heartbeat.ts)

### 3. JARVIS-Sentinel (Deterministic Rollback Engine)
* Maps transactional microservice interactions into dynamic execution graphs.
* Intercepts identity drift, session token escalation, and hallucination loops with **sub-second microservice state rollbacks** before corrupted data cascades to downstream systems.
* **See:** [`docs/02-rollback-safety-engine.md`](docs/02-rollback-safety-engine.md) and [`examples/state_rollback_engine.py`](examples/state_rollback_engine.py)

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
├── README.md                      # System overview and architectural diagrams
├── LICENSE                        # MIT License
├── docs/
│   ├── 01-system-architecture.md  # Specification of Supervisor-Worker DAG orchestration
│   ├── 02-rollback-safety-engine.md # Algorithmic design of Sentinel deterministic rollbacks
│   └── 03-heartbeat-telemetry.md  # Specification for proactive heartbeat loops & telemetry
└── examples/
    ├── agent_orchestrator.py      # Reference abstraction for DAG planning & AST validation
    ├── state_rollback_engine.py   # Reference implementation of graph transaction rollbacks
    └── telemetry_heartbeat.ts     # TypeScript interfaces for workspace liveness & telemetry
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

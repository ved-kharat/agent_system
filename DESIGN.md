# System Design Document

## 🏗️ Architecture Overview
This Agentic AI framework relies entirely on a custom, lightweight orchestrator-worker architecture built explicitly without high-level black-box agent frameworks (e.g., LangChain or CrewAI). This ensures complete, low-overhead control over asynchronous tasks, error tracking, and custom token-streaming parameters.

The system is split into distinct functional layers:
1. **Orchestrator (Main Brain):** Accepts a multi-tier problem, breaks it down dynamically into sequential task slices, maps execution targets, and triggers worker routines.
2. **Retriever Agent:** Handles simulated environment context scanning and raw information extraction.
3. **Analyzer Agent:** Processes and strips raw extraction metadata down to critical structured facts.
4. **Writer Agent:** Assembles the synthesized analysis into a coherent document structure and manages the custom token-by-token terminal printing layout.

## 🔄 System Data Flow Diagram
User Complex Goal
       │
       ▼
[Orchestrator Stage] ──> Breaks down raw intent into discrete pipeline stages
       │
       ├─► [Retriever Worker] ──► Extracts raw background environmental tokens
       │                                  │
       ├─► [Analyzer Worker]  ◄───────────┘ Cleans context data & parses facts
       │                                  │
       └─► [Writer Worker]    ◄───────────┘ Formats summary & streams final log output
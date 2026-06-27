# Engineering Post-Mortem Document

## 📉 1. Projected Scaling Bottleneck Analysis
If this system were instantly scaled to process 10,000 tasks simultaneously, the direct, un-throttled sequential batching pipeline would suffer dramatic performance degradation. Because it lacks a distributed message broker (such as RabbitMQ or Celery) and decoupled background thread workers, the Python event loop would experience heavy blocking during massive concurrent I/O cycles. Memory usage would grow linearly with each concurrent task, leading to high latency spikes across agent pass-offs and eventual system-wide timeouts.

## 🛠️ 2. Architectural Re-design in Hindsight
If rebuilding this application from scratch, I would introduce a centralized key-value state manager (such as a shared context blackboard) instead of passing raw string payloads directly between individual agent function parameters. This structural separation between agent execution and state storage would allow for safer system logging, easier stage telemetry auditing, and the ability to seamlessly pause and resume failed multi-agent workflows.

## ⚖️ 3. Explicit Technical Trade-offs
* **Trade-off 1 (Custom Engine vs. Black-Box Frameworks):** I chose to write native control structures and execution loops over using out-of-the-box libraries like LangChain. *Reasoning:* While frameworks provide fast prototyping, writing a raw engine provides total control over state visibility, keeps the footprint exceptionally lightweight, and explicitly shows token-by-token streaming behavior.
* **Trade-off 2 (Fixed Retry Limits vs. Infinite Polling):** I chose a rigid 3-attempt exponential backoff ceiling for the network error mitigation loop. *Reasoning:* This protects local computing resources and stops the program from hanging indefinitely in a dead loop during permanent third-party outages, though it means a task will gracefully fail if the outage outlasts the retry window.
*
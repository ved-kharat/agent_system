# Asynchronous Multi-Agent AI Script

A lightweight, native multi-agent orchestration architecture written in Python using `asyncio`. It handles multi-stage task execution, processes streaming token generation, and embeds structured network retry resilience loops natively.

## 📂 Project Structure
* `main.py` - Core multi-agent pipeline engine and retry logic hooks.
* `DESIGN.md` - System architecture description and data-flow map.
* `POST_MORTEM.md` - Engineering evaluation on scaling, hindsight improvements, and explicit trade-offs.

## 🚀 How to Run Locally
Ensure you are in the project folder directory via your terminal, then execute:
```bash
python main.py
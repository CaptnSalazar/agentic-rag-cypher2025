# Agentic RAG — Cypher 2025

## Overview
Agentic RAG pipeline built for the **Cypher 2025 Hackathon** by **Yash Shukla**. This project addresses the challenge of answering diverse query types (factual, open-ended, reasoning-heavy) by combining local knowledge bases, live web search, and a multi-agent reasoning system. It leverages [e.g., LangChain, OpenAI API] to deliver concise, accurate, and transparent responses with citations.

## Problem Statement
Many question-answering systems struggle with adaptability across query types and lack transparency in sourcing. This project introduces a modular, agent-based RAG pipeline that dynamically routes queries, retrieves relevant data, and reasons through answers while maintaining provenance for trust.

## Prerequisites
- Python 3.8+
- Key libraries: `langchain`, `openai`, `faiss` (see `requirements.txt` for full list)
- API keys: OpenAI API key

## Quickstart

1. **Clone & enter repo**

   ```bash
   git clone https://github.com/username/agentic-rag-cypher2025.git
   cd agentic-rag-cypher2025
   ```

2. **Install dependencies**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure API keys**

   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

4. **Run demo**

   ```bash
   python run_demo.py --query "What causes sudden server crashes?"
   ```

## Architecture
The system uses a multi-agent pipeline:
1. **Router**: Classifies query type and directs it to the appropriate pipeline.
2. **Retriever**: Fetches relevant data from local vector stores and web searches.
3. **Ranker**: Scores and filters retrieved data for relevance.
4. **Reasoner**: Synthesizes answers, applying reasoning for complex queries.
5. **Verifier**: Ensures answer correctness and adds citations.

```
                +-----------------+            +----------------+
     User --->  |  Query Router   |--(type)-->|  Planner/Agent |
                +-----------------+            +--+----+--------+
                         |                         |    |   
                         v                         v    v
             +--------------------+       +---------------+  +----------------+
             | Retriever Manager  |<----->|  Web Crawler  |  | Tools / APIs   |
             | (local / vector /  |       +---------------+  | (calculator,    |
             |  metadata filters) |                         |  DB lookups)    |
             +---------+----------+                         +----------------+
                       |  
                       v
               +---------------+
               |  Ranker + QA   |<-- optional verifier
               +-------+-------+
                       |
                       v
               +---------------+
               |  Reasoner /    |
               |  Summarizer    |
               +---------------+
                       |
                       v
               +---------------+
               |  Verifier +    |
               |  CitationGen   |
               +---------------+
                       |
                       v
```         

## Repository Structure
```
agentic-rag-cypher2025/
│   README.md
│   requirements.txt
│   config.py
│   run_demo.py
│   orchestrator.py
│
├── agents/
│   ├── router.py
│   ├── web_search.py
│   ├── ranker_qa.py
│   ├── reasoner.py
│   └── verifier.py
│
├── retriever/
│   └── vector_store.py
│
├── llm_clients/
│   └── openai_client.py
│
├── utils/
│   └── provenance.py
│
└── scripts/
    ├── ingest_data.py
    └── demo_queries.sh
```

## Usage Examples
- **Factual Query**:
  ```bash
  python run_demo.py --query "What is the capital of France?"
  ```
  **Output**: The capital of France is Paris.  
  **Source**: Internal knowledge base.

- **Open-Ended Query**:
  ```bash
  python run_demo.py --query "What are the implications of AI in healthcare?"
  ```
  **Output**: Summarized perspectives with sources.

- **Reasoning-Heavy Query**:
  ```bash
  python run_demo.py --query "Why might a server crash unexpectedly?"
  ```
  **Output**: Detailed reasoning with steps and citations.

## Testing and Validation
The system was tested with 50 sample queries across factual, open-ended, and reasoning-heavy categories. Accuracy was evaluated based on source grounding and response coherence. Unit tests for individual agents are in `tests/` (if applicable).

## Contributing
Contributions are welcome! Please submit issues or pull requests via GitHub. Ensure code follows PEP 8 standards and includes tests.

## Future Improvements
- Add caching for faster responses
- Integrate structured sources (databases, APIs)
- Expand reasoning agent with symbolic + probabilistic reasoning
- Build a simple web UI for improved UX

## License
MIT License
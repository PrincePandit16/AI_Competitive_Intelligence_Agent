<div align="center">
<br/>
<h1>🕵️‍♂️ AI Competitive Intelligence Agent</h1>
 
<p><strong>An autonomous multi-LLM agent system that researches companies, analyzes market trends,<br/>and generates verified strategic reports — fully automated, zero manual effort.</strong></p>
<br/>
<!-- Language -->
<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<!-- LLM Providers -->
<img src="https://img.shields.io/badge/Google%20Gemini-Primary%20LLM-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Gemini"/>
<img src="https://img.shields.io/badge/ChatGroq-Fast%20Inference-F55036?style=for-the-badge&logo=groq&logoColor=white" alt="ChatGroq"/>
<img src="https://img.shields.io/badge/HuggingFace-Embeddings-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="HuggingFace"/>
<br/><br/>
 
<!-- Orchestration -->
<img src="https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge" alt="LangChain"/>
<img src="https://img.shields.io/badge/LangGraph-Graph%20Workflow-FF6B35?style=for-the-badge" alt="LangGraph"/>
<img src="https://img.shields.io/badge/LangSmith-Tracing%20%26%20Eval-F7C948?style=for-the-badge" alt="LangSmith"/>
<br/><br/>
 
<!-- Tools -->
<img src="https://img.shields.io/badge/Tavily-AI%20Web%20Search-5865F2?style=for-the-badge" alt="Tavily"/>
<img src="https://img.shields.io/badge/python--dotenv-Env%20Config-ECD53F?style=for-the-badge" alt="python-dotenv"/>
<br/><br/>
 
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License"/>
<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Active"/>
<img src="https://img.shields.io/badge/100%25-Python-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 100%"/>
<br/><br/>
 
<blockquote>
  <strong>Three LLMs. One agentic graph. Zero manual research.</strong><br/>
  Powered by <strong>Google Gemini · ChatGroq · HuggingFace</strong> — orchestrated via <strong>LangGraph</strong>, traced live with <strong>LangSmith</strong>.
</blockquote>
</div>


## 🧠 What It Does

This system uses a graph-based multi-agent workflow to autonomously:

- Plan a research strategy for a given company or market
- Search the web for real-time competitive data using Tavily
- Summarize and synthesize gathered information
- Verify the accuracy and quality of findings
- Generate a structured, final strategic report

All agent interactions are fully observable via LangSmith tracing.

---

## 🏗️ Project Structure

```
AI_Competitive_Intelligence_Agent/
├── app/
│   ├── agents/
│   │   ├── final_reports.py       # Generates the final strategic report
│   │   ├── planner_agent.py       # Plans the research strategy
│   │   ├── research_agent.py      # Performs web research via Tavily
│   │   ├── summarizer_agent.py    # Summarizes gathered data
│   │   └── verifier_agent.py      # Verifies and validates findings
│   ├── graph/
│   │   └── workflow.py            # LangGraph workflow definition
│   ├── llms/
│   │   ├── google_llm.py          # Google Gemini LLM integration
│   │   ├── groq_llm.py            # Groq LLM integration
│   │   └── huggingface_llm.py     # HuggingFace LLM integration
│   ├── models/
│   │   └── state.py               # LangGraph state model
│   ├── prompts/
│   │   ├── planner_prompt.py      # Prompt for the planner agent
│   │   ├── research_prompt.py     # Prompt for the research agent
│   │   ├── summary_prompt.py      # Prompt for the summarizer agent
│   │   └── verification_prompt.py # Prompt for the verifier agent
│   └── tools/                     # Custom tool definitions
├── main.py                        # Entry point
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

---

## ⚙️ Tech Stack

| Component | Technology |
|---|---|
| Agent Orchestration | LangChain + LangGraph |
| LLM Providers | Google Gemini, Groq, HuggingFace |
| Web Search | Tavily Search API |
| Observability | LangSmith |
| Environment Config | python-dotenv |
| Language | Python |

---

## 🔄 Agent Workflow

The system runs as a directed graph powered by **LangGraph**:

```
User Input
    ↓
Planner Agent      →  Breaks the task into a research plan
    ↓
Research Agent     →  Searches the web using Tavily API
    ↓
Summarizer Agent   →  Condenses and synthesizes findings
    ↓
Verifier Agent     →  Validates accuracy and completeness
    ↓
Final Report       →  Produces a structured strategic report
```

Each node in the graph is an independent agent with its own prompt, LLM, and responsibilities.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/PrincePandit16/AI_Competitive_Intelligence_Agent.git
cd AI_Competitive_Intelligence_Agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or with `uv` (recommended):

```bash
uv sync
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
# LLM API Keys
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token

# Tavily Web Search
TAVILY_API_KEY=your_tavily_api_key

# LangSmith Observability
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=AI_Competitive_Intelligence_Agent
```

### 4. Run the Agent

```bash
python main.py
```

---

## 🔍 Observability with LangSmith

This project is integrated with **LangSmith** for full tracing and observability of every agent step. Once `LANGCHAIN_TRACING_V2=true` is set, all agent runs, LLM calls, tool invocations, and graph transitions are automatically logged to your LangSmith dashboard.

Visit [smith.langchain.com](https://smith.langchain.com) to view traces.

---

## 🔑 API Keys Required

| Service | Where to Get It |
|---|---|
| Google Gemini | [Google AI Studio](https://aistudio.google.com/) |
| Groq | [console.groq.com](https://console.groq.com/) |
| HuggingFace | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) |
| Tavily | [app.tavily.com](https://app.tavily.com/) |
| LangSmith | [smith.langchain.com](https://smith.langchain.com/) |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---


<div align="center">
<br/>
Made with 🧠 + ❤️ by PrincePandit16
 
⭐ **If this project helped you, drop a star — it means a lot!**
 
</div>

---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# 🚀 AI Trading

```{code-cell} ipython3
:tags: [remove-input, remove-output]

%load_ext autoreload
%autoreload 2
```

```{code-cell} ipython3
:tags: [remove-input]

from pytrade.table import repos_table
from pytrade.enums import ProjectStatus
```

## AI-Trading Apps

> Disclaimer: I am the creator of 🐘 `alphafund`

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "alphafund": {
        "github": "PFund-Software-Ltd/alphafund",
        "_fetch_github": False,
        "Status": "🚧",
        "Approach": "💻 Code-to-Trade",
        "Backtest": True,
        "Live": True,
        "Research": True,
        "TradFi": True,
        "CeFi": True,
        "DeFi": False,
        "Prediction Market": False,
    },
    "nofx": {
        "github": "NoFxAiOS/nofx",
        "Status": ProjectStatus.ACTIVE,
        "Approach": "Prompt-to-Trade",
        "Backtest": True,
        "Live": True,
        "Research": True,
        "TradFi": False,
        "CeFi": True,
        "DeFi": False,
        "Prediction Market": False,
    },
    "vibe-trading": {
        "github": "HKUDS/Vibe-Trading",
        "Status": ProjectStatus.ACTIVE,
        "Approach": "Prompt-to-Trade",
        "Backtest": True,
        "Live": True,
        "Research": True,
        "TradFi": True,
        "CeFi": True,
        "DeFi": False,
        "Prediction Market": False,
    },
    "finrobot": {
        "github": "ai4finance-foundation/finrobot",
        "Status": ProjectStatus.ACTIVE,
        "Approach": None,
        "Backtest": False,
        "Live": False,
        "Research": True,
        "TradFi": None,
        "CeFi": None,
        "DeFi": None,
        "Prediction Market": None,
    },
    "trading_agents": {
        "github": "tauricresearch/tradingagents",
        "Status": ProjectStatus.ACTIVE,
        "Approach": None,
        "Backtest": False,
        "Live": False,
        "Research": True,
        "TradFi": None,
        "CeFi": None,
        "DeFi": None,
        "Prediction Market": None,
    },
    "ai-hedge-fund": {
        "github": "virattt/ai-hedge-fund",
        "Status": ProjectStatus.ACTIVE,
        "Approach": None,
        "Backtest": False,
        "Live": False,
        "Research": True,
        "TradFi": None,
        "CeFi": None,
        "DeFi": None,
        "Prediction Market": None,
    },
    "dexter": {
        "github": "virattt/dexter",
        "Status": ProjectStatus.ACTIVE,
        "Approach": None,
        "Backtest": False,
        "Live": False,
        "Research": True,
        "TradFi": None,
        "CeFi": None,
        "DeFi": None,
        "Prediction Market": None,
    },
}
repos_table(REPOS)
```

- "✔️" = SUPPORTED
- "✖️" = NOT SUPPORTED
- "➖" = NOT APPLICABLE

:::{attention} 💡 Concepts Explained
:class: dropdown
:icon: false

#### Code-to-Trade Approach
This means asking an {abbr}`LLM (Large Language Model)` to **write Python code**, either using a chosen [algo-trading framework](/algo-trading) or writing ad-hoc code, so that a strategy can be **backtested, traded deterministically, with reproducible results**. A good visual example is QuantConnect's [agents](https://www.quantconnect.com/announcements/20802/assistants-agent-teams-for-systematic-research/p1) ([video](https://www.youtube.com/watch?v=IyNwyZeLd_k)).

#### Prompt-to-Trade Approach
This means giving a prompt to an LLM and letting it make trading decisions non-deterministically, meaning **the same input may produce different results across runs**. In other words, **"Vibe-Trading"**. Think of it as [OpenClaw](https://openclaw.ai/) with trading ability.
A good visual example is [Alpha Arena](https://nof1.ai/), where agents trade based on prompts.

:::


:::{tip} Running LLMs for free
:class: dropdown
:icon: false

In order to run the AI apps, you will need access to LLMs.

**LLM Providers (with generous free-tier limits):**
- [Groq](https://groq.com/)
- [Google](https://ai.google.dev/gemini-api/docs)
- [Cerebras](https://inference-docs.cerebras.ai/quickstart)

**Running Local LLMs:**
- [Ollama](https://github.com/ollama/ollama)
- [LM Studio](https://lmstudio.ai/)
- [Rapid-MLX](https://github.com/raullenchai/Rapid-MLX)
- [Jan](https://github.com/janhq/jan)
:::


:::{note} Remarks
:class: dropdown
:icon: false

- The creator of [AI-Hedge-Fund](https://github.com/virattt/ai-hedge-fund) and [Dexter](https://github.com/virattt/dexter) is **also the founder** of [Financial Datasets](https://www.financialdatasets.ai/), the financial data provider recommended in the projects’ READMEs, but this affiliation is not clearly disclosed.
- [AI-Trader](https://github.com/HKUDS/AI-Trader) is another project from the same organization behind [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading), serving as a prompt-to-trade AI trading platform for AI agents such as OpenClaw, nanobot.
:::

---

:::{dropdown} *Optional*
:open: true
*The frameworks below are only relevant if you want to **assemble your own AI trading app***
:::

## Agent Frameworks

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "pydnatic-ai": {
        "github": "pydantic/pydantic-ai",
        "Status": ProjectStatus.ACTIVE
    },
    "smolagents": {
        "github": "huggingface/smolagents",
        "Status": ProjectStatus.ACTIVE
    },
    "openai-agents": {
        "github": "openai/openai-agents-python",
        "Status": ProjectStatus.ACTIVE
    },
    "agno": {
        "github": "agno-agi/agno",
        "Status": ProjectStatus.ACTIVE
    },
    "crewai": {
        "github": "crewaiinc/crewai",
        "Status": ProjectStatus.ACTIVE
    },
    "deepagents": {
        "github": "langchain-ai/deepagents",
        "Status": ProjectStatus.ACTIVE
    },
    "ag2": {
        "github": "ag2ai/ag2",
        "Status": ProjectStatus.ACTIVE
    },
    "autogen": {
        "github": "microsoft/autogen",
        "Status": ProjectStatus.INACTIVE
    },
    
}
repos_table(REPOS)
```

## LLM Frameworks

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "haystack": {
        "github": "deepset-ai/haystack",
        "Status": ProjectStatus.ACTIVE,
    },
    "langchain": {
        "github": "langchain-ai/langchain",
        "Status": ProjectStatus.ACTIVE,
    },
    "llamaindex": {
        "github": "run-llama/llama_index",
        "Status": ProjectStatus.ACTIVE,
    },
}
repos_table(REPOS)
```

:::{note} Agent vs. LLM frameworks — a fuzzy line
:class: dropdown
:icon: false

These two groups overlap, so don't read the split as rigid. Many tools do
both — `langchain`, for instance, can create agents but is centered on LLM
applications. The grouping reflects each framework's **primary focus**, not
its full capability:

- **LLM frameworks** focus on connecting models to your data — retrieval (RAG),
and ingesting/parsing/indexing documents into something an LLM can use
(e.g. `llamaindex`).
- **Agent frameworks** focus on agentic workflows — giving the model tools,
memory, and multi-step autonomy to *act*.
:::


<!-- :::{note} Verdicts ⚖️ -->
<!-- :class: dropdown -->

<!-- Verdicts are my personal quick takes on selected libraries, written to help Python traders choose a -->
<!-- library that fits their own trading needs: -->
<!-- - {verdict urls will be written here} -->

<!-- They are **OPINIONATED** and may not be perfectly accurate, so treat these notes as practical guidance rather than final judgment. -->

<!-- Verdicts are intentionally short for quick reading. For deeper analysis, see the latest posts on the -->
<!-- [Blog](https://pytrade.org/blog) and labs on the [TradeLabs](https://pytrade.org). -->
<!-- ::: -->

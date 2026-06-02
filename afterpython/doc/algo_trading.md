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

# Algo Trading

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

## Algo Trading Frameworks
> Disclaimer: I am the creator of `pfund`

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "nautilus_trader": {
        "github": "nautechsystems/nautilus_trader",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,  # supports backtesting
        "Live": True,  # supports live trading
        "ML-Native": False,
        "TradFi": True,
        "CeFi": True,
        "DeFi": False,
        "Prediction Market": True,
    },
    "lean": {
        "github": "quantconnect/lean",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": True,
        "ML-Native": False,
        "TradFi": True,
        "CeFi": True,
        "DeFi": False,
        "Prediction Market": False,
    },
    "pfund": {
        "github": "PFund-Software-Ltd/pfund",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": True,
        "ML-Native": True,
        "TradFi": True,
        "CeFi": True,
        "DeFi": False,
        "Prediction Market": False,
    },
    "torchtrade": {
        "github": "TorchTrade/torchtrade",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": True,
        "ML-Native": True,
        "TradFi": True,
        "CeFi": True,
        "DeFi": False,
        "Prediction Market": True,
    },
    "finrl-trading": {
        "github": "AI4Finance-Foundation/FinRL-Trading",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": True,
        "ML-Native": True,
        "TradFi": True,
        "CeFi": False,
        "DeFi": False,
        "Prediction Market": False,
    },
    "vnpy": {
        "github": "vnpy/vnpy",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": True,
        "ML-Native": True,
        "TradFi": True,
        "CeFi": False,
        "DeFi": False,
        "Prediction Market": False,
    },
    "vectorbt": {
        "github": "polakowo/vectorbt",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": False,
        "ML-Native": False,
        "TradFi": None,
        "CeFi": None,
        "DeFi": None,
        "Prediction Market": None,
    },
    "backtesting.py": {
        "github": "kernc/backtesting.py",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": False,
        "ML-Native": False,
        "TradFi": None,
        "CeFi": None,
        "DeFi": None,
        "Prediction Market": None,
    },
    "bt": {
        "github": "pmorissette/bt",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": False,
        "ML-Native": False,
        "TradFi": None,
        "CeFi": None,
        "DeFi": None,
        "Prediction Market": None,
    },
    "pybroker": {
        "github": "edtechre/pybroker",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": False,
        "ML-Native": True,
        "TradFi": None,
        "CeFi": None,
        "DeFi": None,
        "Prediction Market": None,
    },
    "hftbacktest": {
        "github": "nkaz001/hftbacktest",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": True,
        "ML-Native": False,
        "TradFi": False,
        "CeFi": True,
        "DeFi": False,
        "Prediction Market": False,
    },
    "qf-lib": {
        "github": "quarkfin/qf-lib",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": True,
        "ML-Native": False,
        "TradFi": True,
        "CeFi": True,
        "DeFi": False,
        "Prediction Market": False,
    },
    "freqtrade": {
        "github": "freqtrade/freqtrade",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": True,
        "ML-Native": False,
        "TradFi": False,
        "CeFi": True,
        "DeFi": False,
        "Prediction Market": False,
    },
    "hummingbot": {
        "github": "hummingbot/hummingbot",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": True,
        "ML-Native": True,
        "TradFi": False,
        "CeFi": True,
        "DeFi": True,
        "Prediction Market": False,
    },
    "jesse": {
        "github": "jesse-ai/jesse",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": True,
        "ML-Native": False,
        "TradFi": False,
        "CeFi": True,
        "DeFi": False,
        "Prediction Market": False,
    },
    "trading-strategy": {
        "github": "tradingstrategy-ai/trading-strategy",
        "Status": ProjectStatus.ACTIVE,
        "Backtest": True,
        "Live": True,
        "ML-Native": False,
        "TradFi": False,
        "CeFi": False,
        "DeFi": True,
        "Prediction Market": False,
    },
    "backtrader": {
        "github": "mementum/backtrader",
        "Status": ProjectStatus.INACTIVE,
        "Backtest": True,
        "Live": True,
        "ML-Native": False,
        "TradFi": True,
        "CeFi": False,
        "DeFi": False,
        "Prediction Market": False,
    },
    "zipline-reloaded": {
        "github": "stefan-jansen/zipline-reloaded",
        "Status": ProjectStatus.INACTIVE,
        "Backtest": True,
        "Live": False,
        "ML-Native": False,
        "TradFi": None,
        "CeFi": None,
        "DeFi": None,
        "Prediction Market": None,
    },
    "blankly": {
        "github": "Blankly-Finance/blankly",
        "Status": ProjectStatus.UNMAINTAINED,
        "Backtest": True,
        "Live": True,
        "ML-Native": False,
        "TradFi": True,
        "CeFi": True,
        "DeFi": False,
        "Prediction Market": False,
    },
    "qstrader": {
        "github": "mhallsmoore/qstrader",
        "Status": ProjectStatus.UNMAINTAINED,
        "Backtest": True,
        "Live": False,
        "ML-Native": False,
        "TradFi": None,
        "CeFi": None,
        "DeFi": None,
        "Prediction Market": None,
    },
    "qtpylib": {
        "github": "ranaroussi/qtpylib",
        "Status": ProjectStatus.UNMAINTAINED,
        "Backtest": True,
        "Live": True,
        "ML-Native": False,
        "TradFi": True,
        "CeFi": False,
        "DeFi": False,
        "Prediction Market": False,
    },
}
repos_table(REPOS)
```

- "✔️" = SUPPORTED
- "✖️" = NOT SUPPORTED
- "➖" = NOT APPLICABLE


## Hyperparameter Optimization

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "optuna": {
        "github": "optuna/optuna",
        "Status": ProjectStatus.ACTIVE,
    },
    "botorch": {
        "github": "meta-pytorch/botorch",
        "Status": ProjectStatus.ACTIVE,
    },
    "bayesian-optimization": {
        "github": "bayesian-optimization/BayesianOptimization",
        "Status": ProjectStatus.ACTIVE,
    },
}

repos_table(REPOS)
```

## Research & Exploration

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "openbb": {
        "github": "OpenBB-finance/OpenBB",
        "Status": ProjectStatus.ACTIVE,
    },
    "fincept-terminal": {
        "github": "Fincept-Corporation/FinceptTerminal",
        "Status": ProjectStatus.ACTIVE,
    },
    "qlib": {
        "github": "microsoft/qlib",
        "Status": ProjectStatus.ACTIVE,
    },
    "finrl": {
        "github": "AI4Finance-Foundation/FinRL",
        "Status": ProjectStatus.ACTIVE,
    },
    "finmarketpy": {
        "github": "cuemacro/finmarketpy",
        "Status": ProjectStatus.ACTIVE,
    },
}

repos_table(REPOS)
```

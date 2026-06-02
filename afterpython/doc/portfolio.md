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

# Portfolio, Analytics & Analysis

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

## Portfolio Optimization & Metrics

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "skfolio": {
        "github": "skfolio/skfolio",
        "Status": ProjectStatus.ACTIVE,
    },
    "cvxportfolio": {
        "github": "cvxgrp/cvxportfolio",
        "Status": ProjectStatus.ACTIVE,
    },
    "PyPortfolioOpt": {
        "github": "PyPortfolio/PyPortfolioOpt",
        "Status": ProjectStatus.ACTIVE,
    },
    "riskfolio-lib": {
        "github": "dcajasn/Riskfolio-Lib",
        "Status": ProjectStatus.ACTIVE,
    },
    "FinQuant": {
        "github": "fmilthaler/FinQuant",
        "Status": ProjectStatus.UNMAINTAINED
    },
}
repos_table(REPOS)
```

## Trading Analytics

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
     "jquantstats": {
         "github": "jebel-quant/jquantstats",
         "Status": ProjectStatus.ACTIVE,
     },
     "ffn": {
         "github": "pmorissette/ffn",
         "Status": ProjectStatus.ACTIVE,
     },
     "quantstats": {
         "github": "ranaroussi/quantstats",
         "Status": ProjectStatus.ACTIVE,
     },
     "pyfolio-reloaded": {
         "github": "stefan-jansen/pyfolio-reloaded",
         "Status": ProjectStatus.INACTIVE,
     },
    "empyrical-reloaded": {
         "github": "stefan-jansen/empyrical-reloaded",
         "Status": ProjectStatus.INACTIVE,
     },
    
}
repos_table(REPOS)
```

## Factor Analysis

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "alphalens-reloaded": {
         "github": "stefan-jansen/alphalens-reloaded",
         "Status": ProjectStatus.INACTIVE,
     },
}
repos_table(REPOS)
```

## Technical Analysis

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "talib": {
        "github": "TA-Lib/ta-lib-python",
        "Status": ProjectStatus.ACTIVE,
    },
    "pandas-ta-classic": {
        "github": "xgboosted/pandas-ta-classic",
        "Status": ProjectStatus.ACTIVE,
    },
    "freqtrade-technical": {
        "github": "freqtrade/technical",
        "Status": ProjectStatus.ACTIVE,
    },
    "stockstats": {
        "github": "jealous/stockstats",
        "Status": ProjectStatus.ACTIVE
    },    
    "ta": {
        "github": "bukosabino/ta",
        "Status": ProjectStatus.UNMAINTAINED,
    },
}
repos_table(REPOS)
```

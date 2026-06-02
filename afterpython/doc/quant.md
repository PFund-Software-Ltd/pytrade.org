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

# Quant Libraries

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

## Quantitative Finance

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "quantlib": {
        "github": "quantlib/QuantLib",
        "Status": ProjectStatus.ACTIVE,  
    },
    "financepy": {
        "github": "domokane/financepy",
        "Status": ProjectStatus.ACTIVE,  
    },
    "gs-quant": {
        "github": "goldmansachs/gs-quant",
        "Status": ProjectStatus.ACTIVE,  
    },
    "vollib": {
        "github": "vollib/py_vollib",
        "Status": ProjectStatus.ACTIVE,  
    },
    "rateslib": {
        "github": "attack68/rateslib",
        "Status": ProjectStatus.ACTIVE,  
    },
    "tf-quant-finance": {
        "github": "google/tf-quant-finance",
        "Status": ProjectStatus.UNMAINTAINED,  
    },
}

repos_table(REPOS)
```

> `gs-quant` doc is here: https://developer.gs.com/docs/gsquant/


## Time Series Analysis

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "sktime": {
        "github": "sktime/sktime",
        "Status": ProjectStatus.ACTIVE,  
    },
    "pytorch-forecasting": {
        "github": "sktime/pytorch-forecasting",
        "Status": ProjectStatus.ACTIVE,  
    },
    "tsai": {
        "github": "timeseriesAI/tsai",
        "Status": ProjectStatus.ACTIVE,  
    },
    "skforecast": {
        "github": "skforecast/skforecast",
        "Status": ProjectStatus.ACTIVE,  
    },
    "statsforecast": {
        "github": "Nixtla/statsforecast",
        "Status": ProjectStatus.ACTIVE,  
    },
    "mlforecast": {
        "github": "Nixtla/mlforecast",
        "Status": ProjectStatus.ACTIVE,  
    },
    "neuralforecast": {
        "github": "Nixtla/neuralforecast",
        "Status": ProjectStatus.ACTIVE,  
    },
    "tslearn": {
        "github": "tslearn-team/tslearn",
        "Status": ProjectStatus.ACTIVE,  
    },
    "stumpy": {
        "github": "stumpy-dev/stumpy",
        "Status": ProjectStatus.ACTIVE,  
    },
    "pytimetk": {
        "github": "business-science/pytimetk",
        "Status": ProjectStatus.ACTIVE,  
    },
    "darts": {
        "github": "unit8co/darts",
        "Status": ProjectStatus.ACTIVE,  
    },
    "pyod": {
        "github": "yzhao062/pyod",
        "Status": ProjectStatus.ACTIVE,  
    },
    "gluonts": {
        "github": "awslabs/gluonts",
        "Status": ProjectStatus.ACTIVE,  
    },
    "arch": {
        "github": "bashtage/arch",
        "Status": ProjectStatus.ACTIVE,  
    },
}

repos_table(REPOS)
```

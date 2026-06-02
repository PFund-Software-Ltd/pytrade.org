---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.3
kernelspec:
  name: python3
  language: python
  display_name: Python 3 (ipykernel)
---

# Visualization

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

## Plotting Libraries

> Disclaimer: I am the creator of `pfund-plot`

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "plotly": {
        "github": "plotly/plotly.py",
        "Status": ProjectStatus.ACTIVE,
    },
    "bokeh": {
        "github": "bokeh/bokeh",
        "Status": ProjectStatus.ACTIVE,
    },
    "altair": {
        "github": "vega/altair",
        "Status": ProjectStatus.ACTIVE,
    },
    "hvplot": {
        "github": "holoviz/hvplot",
        "Status": ProjectStatus.ACTIVE,
    },
    "pfund-plot": {
        "github": "PFund-Software-Ltd/pfund-plot",
        "Status": ProjectStatus.ACTIVE,  
    },
    "matplotlib": {
        "github": "matplotlib/matplotlib",
        "Status": ProjectStatus.ACTIVE,
    },
    "plotnine": {
        "github": "has2k1/plotnine",
        "Status": ProjectStatus.ACTIVE,
    },
    "pyecharts": {
        "github": "pyecharts/pyecharts",
        "Status": ProjectStatus.ACTIVE,
    },
    "perspective": {
        "github": "perspective-dev/perspective",
        "Status": ProjectStatus.ACTIVE,
    },
}

repos_table(REPOS)
```

## Dashboards

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "streamlit": {
        "github": "streamlit/streamlit",
        "Status": ProjectStatus.ACTIVE,
    },
    "gradio": {
        "github": "gradio-app/gradio",
        "Status": ProjectStatus.ACTIVE,
    },
    "dash": {
        "github": "plotly/dash",
        "Status": ProjectStatus.ACTIVE,
    },
    "panel": {
        "github": "holoviz/panel",
        "Status": ProjectStatus.ACTIVE,
    },
    "taipy": {
        "github": "avaiga/taipy",
        "Status": ProjectStatus.ACTIVE,
    },
    "shiny": {
        "github": "posit-dev/py-shiny",
        "Status": ProjectStatus.ACTIVE,
    },
    "solara": {
        "github": "widgetti/solara",
        "Status": ProjectStatus.ACTIVE,
    },
}

repos_table(REPOS)
```

## Data Exploration

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "data-formulator": {
        "github": "microsoft/data-formulator",
        "Status": ProjectStatus.ACTIVE,
    },
    "pygwalker": {
        "github": "Kanaries/pygwalker",
        "Status": ProjectStatus.ACTIVE,
    },
    "lumen": {
        "github": "holoviz/lumen",
        "Status": ProjectStatus.ACTIVE,
    },
    "fg-data-profiling": {
        "github": "Data-Centric-AI-Community/fg-data-profiling",
        "Status": ProjectStatus.ACTIVE,
    },
}

repos_table(REPOS)
```

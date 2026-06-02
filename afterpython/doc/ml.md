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

# Machine Learning & Statistics

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

## Machine/Deep/Reinforcement Learning

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "sklearn": {
        "github": "scikit-learn/scikit-learn",
        "Status": ProjectStatus.ACTIVE,
    },
    "transformers": {
        "github": "huggingface/transformers",
        "Status": ProjectStatus.ACTIVE,
    },
    "torch": {
        "github": "pytorch/pytorch",
        "Status": ProjectStatus.ACTIVE,
    },
    "jax": {
        "github": "jax-ml/jax",
        "Status": ProjectStatus.ACTIVE,
    },
    "tinygrad": {
        "github": "tinygrad/tinygrad",
        "Status": ProjectStatus.ACTIVE,
    },
    "tensorflow": {
        "github": "tensorflow/tensorflow",
        "Status": ProjectStatus.ACTIVE,
    },
    "keras": {
        "github": "keras-team/keras",
        "Status": ProjectStatus.ACTIVE,
    },
    "torchrl": {
        "github": "pytorch/rl",
        "Status": ProjectStatus.ACTIVE,
    },
    "skrl": {
        "github": "toni-sm/skrl",
        "Status": ProjectStatus.ACTIVE,
    },
    "cleanrl": {
        "github": "vwxyzjn/cleanrl",
        "Status": ProjectStatus.ACTIVE,
    },
    
}
repos_table(REPOS)
```

## Bayesian Statistics / Probabilistic Programming

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    'numpyro': {
        "github": "pyro-ppl/numpyro",
        "Status": ProjectStatus.ACTIVE,
    },
    "pymc": {
        "github": "pymc-devs/pymc",
        "Status": ProjectStatus.ACTIVE,
    },
    "stan": {
        "github": "stan-dev/pystan",
        "Status": ProjectStatus.ACTIVE,
    },
    "pyro": {
        "github": "pyro-ppl/pyro",
        "Status": ProjectStatus.INACTIVE,
    },
    "tfp": {
        "github": "tensorflow/probability",
        "Status": ProjectStatus.INACTIVE,
    },
}
repos_table(REPOS)
```

## Feature Engineering

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "feature-engine": {
        "github": "feature-engine/feature_engine",
        "Status": ProjectStatus.ACTIVE,
    },
    "tsfresh": {
        "github": "blue-yonder/tsfresh",
        "Status": ProjectStatus.ACTIVE,
    },
    "category_encoders": {
        "github": "scikit-learn-contrib/category_encoders",
        "Status": ProjectStatus.ACTIVE,
    },
    "featuretools": {
        "github": "alteryx/featuretools",
        "Status": ProjectStatus.UNMAINTAINED,
    },
}
repos_table(REPOS)
```

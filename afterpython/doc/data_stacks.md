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

# Data Stacks

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

## Data Libraries

> Disclaimer: I am the creator of `pfeed`

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "pfeed": {
        "github": "PFund-Software-Ltd/pfeed",
        "Status": ProjectStatus.ACTIVE,
        "Historical Data": True,
        "Streaming Data": True,
    },
    "defeat-beta": {
        "github": "defeat-beta/defeatbeta-api",
        "Status": ProjectStatus.ACTIVE,
        "Historical Data": True,
        "Streaming Data": False,
    },
    "yfinance": {
        "github": "ranaroussi/yfinance",
        "Status": ProjectStatus.ACTIVE,
        "Historical Data": True,
        "Streaming Data": True,
    },
    "ccxt": {
        "github": "ccxt/ccxt",
        "Status": ProjectStatus.ACTIVE,
        "Historical Data": False,
        "Streaming Data": True,
    },
    "FinanceDatabase": {
        "github": "jerbouma/FinanceDatabase",
        "Status": ProjectStatus.ACTIVE,
        "Historical Data": True,
        "Streaming Data": False,
    },
    "cryptofeed": {
        "github": "bmoscon/cryptofeed",
        "Status": ProjectStatus.INACTIVE,
        "Historical Data": False,
        "Streaming Data": True,
    },
    "binance-public-data": {
        "github": "binance/binance-public-data",
        "Status": ProjectStatus.INACTIVE,
        "Historical Data": True,
        "Streaming Data": False,
    },
}

repos_table(REPOS)
```

- "✔️" = SUPPORTED
- "✖️" = NOT SUPPORTED

:::{seealso}
For SDKs related to specific data providers, please go to [Data Sources](./data_sources.md)
:::


## Data Tools

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "polars": {
        "github": "pola-rs/polars",
        "Status": ProjectStatus.ACTIVE,
    },
    "daft": {
        "github": "eventual-inc/daft",
        "Status": ProjectStatus.ACTIVE,
    },
    "pandas": {
        "github": "pandas-dev/pandas",
        "Status": ProjectStatus.ACTIVE,
    },
    "dask": {
        "github": "dask/dask",
        "Status": ProjectStatus.ACTIVE,
    },
    "spark": {
        "github": "apache/spark",
        "Status": ProjectStatus.ACTIVE,
    },
    "bodo": {
        "github": "bodo-ai/Bodo",
        "Status": ProjectStatus.ACTIVE,
    },
    "ibis": {
        "github": "ibis-project/ibis",
        "Status": ProjectStatus.ACTIVE,
    },
    "fugue": {
        "github": "fugue-project/fugue",
        "Status": ProjectStatus.ACTIVE,
    },
    "vaex": {
        "github": "vaexio/vaex",
        "Status": ProjectStatus.ACTIVE,
    },
    "datafusion": {
        "github": "apache/datafusion",
        "Status": ProjectStatus.ACTIVE,
    },
    "velox": {
        "github": "facebookincubator/velox",
        "Status": ProjectStatus.ACTIVE,
    },
    "sqlglot": {
        "github": "tobymao/sqlglot",
        "Status": ProjectStatus.ACTIVE,
    },
    "modin": {
        "github": "modin-project/modin",
        "Status": ProjectStatus.INACTIVE,
    },
}

repos_table(REPOS)
```

## Data Formats & Storage

> Only installable databases are considered storage

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "duckdb": {
        "github": "duckdb/duckdb",
        "Status": ProjectStatus.ACTIVE,
    },
    "lancedb": {
        "github": "lancedb/lancedb",
        "Status": ProjectStatus.ACTIVE,
    },
    "chdb": {
        "github": "chdb-io/chdb",
        "Status": ProjectStatus.ACTIVE,
    },
    "arcticdb": {
        "github": "man-group/arcticdb",
        "Status": ProjectStatus.ACTIVE,
    },
    "sqlite": {
        "github": "sqlite/sqlite",
        "Status": ProjectStatus.ACTIVE,
    },
    "arrow": {
        "github": "apache/arrow",
        "Status": ProjectStatus.ACTIVE,
    },
    "parquet": {
        "github": "apache/parquet-format",
        "Status": ProjectStatus.ACTIVE,
    },
    "vortex": {
        "github": "vortex-data/vortex",
        "Status": ProjectStatus.ACTIVE,
    },
    "deltalake": {
        "github": "delta-io/delta-rs",
        "Status": ProjectStatus.ACTIVE,
    },
    "iceberg": {
        "github": "apache/iceberg-python",
        "Status": ProjectStatus.ACTIVE,
    },
    "ducklake": {
        "github": "duckdb/ducklake",
        "Status": ProjectStatus.ACTIVE,
    },
    "avro": {
        "github": "apache/avro",
        "Status": ProjectStatus.ACTIVE,
    },
    "hdf5": {
        "github": "HDFGroup/hdf5",
        "Status": ProjectStatus.ACTIVE,
    },
}

repos_table(REPOS)
```

## Data Streaming

```{code-cell} ipython3
:tags: [remove-input]

REPOS ={
    "pathway": {
        "github": "pathwaycom/pathway",
        "Status": ProjectStatus.ACTIVE,
    },
    "csp": {
        "github": "Point72/csp",
        "Status": ProjectStatus.ACTIVE,
    },
    "quix-stream": {
        "github": "quixio/quix-streams",
        "Status": ProjectStatus.ACTIVE,
    },
    "faststream": {
        "github": "ag2ai/faststream",
        "Status": ProjectStatus.ACTIVE,
    },
    "bytewax": {
        "github": "bytewax/bytewax",
        "Status": ProjectStatus.UNMAINTAINED,
    },
}

repos_table(REPOS)
```

## Data Preparation & Validation

```{code-cell} ipython3
:tags: [remove-input]

REPOS ={
    "cleanlab": {
        "github": "cleanlab/cleanlab",
        "Status": ProjectStatus.ACTIVE,
    },
    "skrub": {
        "github": "skrub-data/skrub",
        "Status": ProjectStatus.ACTIVE,
    },
    "pyjanitor": {
        "github": "pyjanitor-devs/pyjanitor",
        "Status": ProjectStatus.ACTIVE,
    },
    "pandera": {
        "github": "unionai-oss/pandera",
        "Status": ProjectStatus.ACTIVE,
    },
    "pointblank": {
        "github": "posit-dev/pointblank",
        "Status": ProjectStatus.ACTIVE,
    },
    "dataframely": {
        "github": "quantco/dataframely",
        "Status": ProjectStatus.ACTIVE,
    },
    "great_expectations": {
        "github": "great-expectations/great_expectations",
        "Status": ProjectStatus.ACTIVE,
    },
}

repos_table(REPOS)
```

## Data Orchestration

```{code-cell} ipython3
:tags: [remove-input]

REPOS = {
    "prefect": {
        "github": "PrefectHQ/prefect",
        "Status": ProjectStatus.ACTIVE,
    },
    "dagster": {
        "github": "dagster-io/dagster",
        "Status": ProjectStatus.ACTIVE,
    },
    "mage": {
        "github": "mage-ai/mage-ai",
        "Status": ProjectStatus.ACTIVE,
    },
    "airflow": {
        "github": "apache/airflow",
        "Status": ProjectStatus.ACTIVE,
    },
    "kestra": {
        "github": "kestra-io/kestra",
        "Status": ProjectStatus.ACTIVE,
    },
    "kedro": {
        "github": "kedro-org/kedro",
        "Status": ProjectStatus.ACTIVE,
    },
}

repos_table(REPOS)
```

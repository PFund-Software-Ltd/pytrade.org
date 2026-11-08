# /// script
# requires-python = ">=3.13"
# dependencies = ["marimo==0.25.2", "pytrade", "httpx2==2.16.0", "python-dotenv==1.2.4"]
#
# [tool.uv.sources]
# pytrade = { path = "../..", editable = true }
# ///
import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Data Stacks
    """)
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _():
    from pytrade.table import repos_table
    from pytrade.enums import ProjectStatus

    return ProjectStatus, repos_table


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Libraries

    > Disclaimer: I am the creator of `pfeed`
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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

    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - "✓" = SUPPORTED
    - "✗" = NOT SUPPORTED

    :::{seealso}
    For SDKs related to specific data providers, please go to [Data Providers](./data_providers.md)
    :::

    ## Data Tools
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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

    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Formats & Storage

    > Only installable databases are considered storage
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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

    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Streaming
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS ={
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

    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Preparation & Validation
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS ={
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

    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Orchestration
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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

    repos_table(_REPOS)
    return


if __name__ == "__main__":
    app.run()

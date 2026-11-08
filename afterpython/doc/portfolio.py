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
    # Portfolio, Analytics & Analysis
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
    ## Portfolio Optimization & Metrics
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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
    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Trading Analytics
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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
    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Factor Analysis
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
        "alphalens-reloaded": {
             "github": "stefan-jansen/alphalens-reloaded",
             "Status": ProjectStatus.INACTIVE,
         },
    }
    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Technical Analysis
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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
    repos_table(_REPOS)
    return


if __name__ == "__main__":
    app.run()

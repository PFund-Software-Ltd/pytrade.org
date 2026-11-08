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
    # Quant Libraries
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
    ## Quantitative Finance
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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
        "lacuna": {
            "github": "eyenoticeall/Lacuna",
            "Status": ProjectStatus.ACTIVE,
        },
        "tf-quant-finance": {
            "github": "google/tf-quant-finance",
            "Status": ProjectStatus.UNMAINTAINED,  
        },
    }

    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > `gs-quant` doc is here: https://developer.gs.com/docs/gsquant/

    ## Time Series Analysis
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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

    repos_table(_REPOS)
    return


if __name__ == "__main__":
    app.run()

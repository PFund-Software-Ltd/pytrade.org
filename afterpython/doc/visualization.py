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
    # Visualization
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
    ## Plotting Libraries

    > Disclaimer: I am the creator of `pfund-plot`
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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

    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dashboards
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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

    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Exploration
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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

    repos_table(_REPOS)
    return


if __name__ == "__main__":
    app.run()

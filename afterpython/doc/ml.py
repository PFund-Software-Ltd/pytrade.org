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
    # Machine Learning & Statistics
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
    ## Machine/Deep/Reinforcement Learning
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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
    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Bayesian Statistics / Probabilistic Programming
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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
    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Feature Engineering
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
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
    repos_table(_REPOS)
    return


if __name__ == "__main__":
    app.run()

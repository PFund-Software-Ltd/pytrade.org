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
    # Algo Trading
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
    ## Algo Trading Frameworks
    > Disclaimer: I am the creator of `pfund`
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
        "nautilus_trader": {
            "github": "nautechsystems/nautilus_trader",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,  # supports backtesting
            "Live": True,  # supports live trading
            "ML-Native": False,
            "TradFi": True,
            "CeFi": True,
            "DeFi": False,
            "Prediction Market": True,
        },
        "lean": {
            "github": "quantconnect/lean",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": True,
            "ML-Native": False,
            "TradFi": True,
            "CeFi": True,
            "DeFi": False,
            "Prediction Market": False,
        },
        "pfund": {
            "github": "PFund-Software-Ltd/pfund",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": True,
            "ML-Native": True,
            "TradFi": True,
            "CeFi": True,
            "DeFi": False,
            "Prediction Market": False,
        },
        "torchtrade": {
            "github": "TorchTrade/torchtrade",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": True,
            "ML-Native": True,
            "TradFi": True,
            "CeFi": True,
            "DeFi": False,
            "Prediction Market": True,
        },
        "finrl-trading": {
            "github": "AI4Finance-Foundation/FinRL-Trading",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": True,
            "ML-Native": True,
            "TradFi": True,
            "CeFi": False,
            "DeFi": False,
            "Prediction Market": False,
        },
        "vnpy": {
            "github": "vnpy/vnpy",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": True,
            "ML-Native": True,
            "TradFi": True,
            "CeFi": False,
            "DeFi": False,
            "Prediction Market": False,
        },
        "vectorbt": {
            "github": "polakowo/vectorbt",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": False,
            "ML-Native": False,
            "TradFi": None,
            "CeFi": None,
            "DeFi": None,
            "Prediction Market": None,
        },
        "backtesting.py": {
            "github": "kernc/backtesting.py",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": False,
            "ML-Native": False,
            "TradFi": None,
            "CeFi": None,
            "DeFi": None,
            "Prediction Market": None,
        },
        "bt": {
            "github": "pmorissette/bt",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": False,
            "ML-Native": False,
            "TradFi": None,
            "CeFi": None,
            "DeFi": None,
            "Prediction Market": None,
        },
        "pybroker": {
            "github": "edtechre/pybroker",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": False,
            "ML-Native": True,
            "TradFi": None,
            "CeFi": None,
            "DeFi": None,
            "Prediction Market": None,
        },
        "hftbacktest": {
            "github": "nkaz001/hftbacktest",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": True,
            "ML-Native": False,
            "TradFi": False,
            "CeFi": True,
            "DeFi": False,
            "Prediction Market": False,
        },
        "qf-lib": {
            "github": "quarkfin/qf-lib",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": True,
            "ML-Native": False,
            "TradFi": True,
            "CeFi": True,
            "DeFi": False,
            "Prediction Market": False,
        },
        "freqtrade": {
            "github": "freqtrade/freqtrade",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": True,
            "ML-Native": False,
            "TradFi": False,
            "CeFi": True,
            "DeFi": False,
            "Prediction Market": False,
        },
        "hummingbot": {
            "github": "hummingbot/hummingbot",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": True,
            "ML-Native": True,
            "TradFi": False,
            "CeFi": True,
            "DeFi": True,
            "Prediction Market": False,
        },
        "jesse": {
            "github": "jesse-ai/jesse",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": True,
            "ML-Native": False,
            "TradFi": False,
            "CeFi": True,
            "DeFi": False,
            "Prediction Market": False,
        },
        "trading-strategy": {
            "github": "tradingstrategy-ai/trading-strategy",
            "Status": ProjectStatus.ACTIVE,
            "Backtest": True,
            "Live": True,
            "ML-Native": False,
            "TradFi": False,
            "CeFi": False,
            "DeFi": True,
            "Prediction Market": False,
        },
        "backtrader": {
            "github": "mementum/backtrader",
            "Status": ProjectStatus.INACTIVE,
            "Backtest": True,
            "Live": True,
            "ML-Native": False,
            "TradFi": True,
            "CeFi": False,
            "DeFi": False,
            "Prediction Market": False,
        },
        "zipline-reloaded": {
            "github": "stefan-jansen/zipline-reloaded",
            "Status": ProjectStatus.INACTIVE,
            "Backtest": True,
            "Live": False,
            "ML-Native": False,
            "TradFi": None,
            "CeFi": None,
            "DeFi": None,
            "Prediction Market": None,
        },
        "blankly": {
            "github": "Blankly-Finance/blankly",
            "Status": ProjectStatus.UNMAINTAINED,
            "Backtest": True,
            "Live": True,
            "ML-Native": False,
            "TradFi": True,
            "CeFi": True,
            "DeFi": False,
            "Prediction Market": False,
        },
        "qstrader": {
            "github": "mhallsmoore/qstrader",
            "Status": ProjectStatus.UNMAINTAINED,
            "Backtest": True,
            "Live": False,
            "ML-Native": False,
            "TradFi": None,
            "CeFi": None,
            "DeFi": None,
            "Prediction Market": None,
        },
        "qtpylib": {
            "github": "ranaroussi/qtpylib",
            "Status": ProjectStatus.UNMAINTAINED,
            "Backtest": True,
            "Live": True,
            "ML-Native": False,
            "TradFi": True,
            "CeFi": False,
            "DeFi": False,
            "Prediction Market": False,
        },
    }
    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - "✓" = SUPPORTED
    - "✗" = NOT SUPPORTED
    - "—" = NOT APPLICABLE

    ## Hyperparameter Optimization
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
        "optuna": {
            "github": "optuna/optuna",
            "Status": ProjectStatus.ACTIVE,
        },
        "botorch": {
            "github": "meta-pytorch/botorch",
            "Status": ProjectStatus.ACTIVE,
        },
        "bayesian-optimization": {
            "github": "bayesian-optimization/BayesianOptimization",
            "Status": ProjectStatus.ACTIVE,
        },
    }

    repos_table(_REPOS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Research & Exploration
    """)
    return


@app.cell(hide_code=True)
def _(ProjectStatus, repos_table):
    _REPOS = {
        "openbb": {
            "github": "OpenBB-finance/OpenBB",
            "Status": ProjectStatus.ACTIVE,
        },
        "fincept-terminal": {
            "github": "Fincept-Corporation/FinceptTerminal",
            "Status": ProjectStatus.ACTIVE,
        },
        "qlib": {
            "github": "microsoft/qlib",
            "Status": ProjectStatus.ACTIVE,
        },
        "finrl": {
            "github": "AI4Finance-Foundation/FinRL",
            "Status": ProjectStatus.ACTIVE,
        },
        "finmarketpy": {
            "github": "cuemacro/finmarketpy",
            "Status": ProjectStatus.ACTIVE,
        },
    }

    repos_table(_REPOS)
    return


if __name__ == "__main__":
    app.run()

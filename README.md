<img src="./public/logo.jpg" width="160"> 

[![Twitter Follow](https://img.shields.io/twitter/follow/pytradeorg?style=social)](https://x.com/pytradeorg)


# Python packages and resources for algo-trading

Inspired by [PyViz](https://pyviz.org/), [PyTrade](https://pytrade.org) is a website showing a curated list of Python libraries and resources for algorithmic trading.
Think of it as an **awesome-algo-trading** list on GitHub, but with a better presentation.

> This website is owned by [PFund.ai](https://pfund.ai), a trading platform that bridges algo-trading and manual trading using AI (LLM).

### Table of Contents
- [Trading Frameworks](https://pytrade.org/trading), full-fledged frameworks that support backtesting, live trading etc.
- [Backtesting Frameworks](https://pytrade.org/backtest), do **NOT** support live trading
- [Strategies](https://pytrade.org/strategies), shared trading strategies, examples and templates
- [Models](https://pytrade.org/models), shared machine learning models for trading 
- [Time Series Analysis](https://pytrade.org/ts_analysis), for analyzing time series data
- [Analytics](https://pytrade.org/analytics), for showing performance metrics
- [Backtesting Data](https://pytrade.org/backtest_data), providing data for backtesting, free or paid
- [Live Trading Data](https://pytrade.org/live_data), providing data for live trading
- [Data Libraries](https://pytrade.org/data_libs), for getting data from the data sources
- [Machine Learning Tools](https://pytrade.org/ml_tools), for applying machine learning on data
- [MLOps Tools](https://pytrade.org/mlops_tools), for applying machine learning operations
- [Data Tools](https://pytrade.org/data_tools), for manipulating data, e.g. pandas
- [Research Tools](https://pytrade.org/researches), for doing research on data
- [Dashboard Tools](https://pytrade.org/dashboards), for creating dashboards for trading
- [Brokers & Exchanges](https://pytrade.org/trading_venues), providing APIs to support algo-trading
- [GPU Providers](https://pytrade.org/gpu_providers), providing GPUs to speed up training
- [API Integrations](https://pytrade.org/api_integrations), integrating with trading APIs without any frameworks
- [Competitions](https://pytrade.org/competitions), for algo-trading competitions
- [Resources](https://pytrade.org/resources), other resources about algo-trading


### Installation
```bash
pnpm install
```


### Development
```bash
pnpm dev
```


### Build Static Files & Run
```bash
pnpm build && pnpm start
```


## Curated List

### Trading Frameworks (support backtesting and live trading)
- [Lean](https://github.com/QuantConnect/Lean)  -  Lean Algorithmic Trading Engine by QuantConnect (Python, C#) 
- [nautilus_trader](https://github.com/nautechsystems/nautilus_trader)  -  A high-performance algorithmic trading platform and event-driven backtester
- [backtrader](https://github.com/mementum/backtrader)  -  Python Backtesting library for trading strategies
- [pfund](https://github.com/PFund-Software-Ltd/pfund)  -  An All-in-One Algo-Trading Framework: Backtest -> Train -> Trade -> Monitor. Machine / Deep Learning Ready. Supports All Trading: TradFi+CeFi+DeFi. Code Once, Trade Anywhere.
- [trading-strategy](https://github.com/tradingstrategy-ai/trading-strategy)  -  Python framework for quantitative financial analysis and trading algorithms on decentralised exchanges
- [blankly](https://github.com/blankly-finance/blankly)  -  🚀 💸 Easily build, backtest and deploy your algo in just a few lines of code. Trade stocks, cryptos, and forex across exchanges w/ one package.
- [vnpy](https://github.com/vnpy/vnpy)  -  a Python-based open source quantitative trading system development framework
- [freqtrade](https://github.com/freqtrade/freqtrade)  -  Free, open source crypto trading bot
- [hummingbot](https://github.com/hummingbot/hummingbot)  -  Open source software that helps you create and deploy high-frequency crypto trading bots
- [jesse](https://github.com/jesse-ai/jesse)  -  An advanced crypto trading bot written in Python
- [Superalgos](https://github.com/Superalgos/Superalgos)  -  Free, open-source crypto trading bot, automated bitcoin / cryptocurrency trading software, algorithmic trading bots. Visually design your crypto trading bot, leveraging an integrated charting system, data-mining, backtesting, paper trading, and multi-server crypto bot deployments.
- [qstrader](https://github.com/mhallsmoore/qstrader)  -  QuantStart.com - QSTrader backtesting simulation engine.
- [qtpylib](https://github.com/ranaroussi/qtpylib)  -  QTPyLib, Pythonic Algorithmic Trading
- [Zipline-reloaded](https://github.com/stefan-jansen/zipline-reloaded)  -  Zipline, a Pythonic Algorithmic Trading Library

### Backtesting Frameworks (only support backtesting)
- [vectorbt](https://github.com/polakowo/vectorbt)  -  Find your trading edge using the fastest engine for backtesting, algorithmic trading, and research.
- [bt](https://github.com/pmorissette/bt)  -  Flexible backtesting library for Python.
- [pybroker](https://github.com/edtechre/pybroker)  -  Algorithmic trading in Python with machine learning.
- [backtesting.py](https://github.com/kernc/backtesting.py)  -  🔍 📈 🐍 💰 Backtest trading strategies in Python.

### Trading Strategies
- [Strategies on QuantConnect](https://www.quantconnect.com/learning/articles/investment-strategy-library)

### Machine Learning Models

### Time Series Analysis
- [tsai](https://github.com/timeseriesAI/tsai)  -   Time series Timeseries Deep Learning Machine Learning Python Pytorch fastai | State-of-the-art Deep Learning library for Time Series and Sequences in Pytorch / fastai
- [stumpy](https://github.com/TDAmeritrade/stumpy)  -  STUMPY is a powerful and scalable Python library for modern time series analysis
- [tsfresh](https://github.com/blue-yonder/tsfresh)  -   Automatic extraction of relevant features from time series
- [sktime](https://github.com/sktime/sktime)  -  A unified framework for machine learning with time series
- [tslearn](https://github.com/tslearn-team/tslearn)  -  The machine learning toolkit for time series analysis in Python
- [arch](https://github.com/bashtage/arch)  -  ARCH models in Python
- [pyod](https://github.com/yzhao062/pyod)  -  A Python library for outlier and anomaly detection, integrating classical and deep learning techniques

### Analytics
- [quantstats](https://github.com/ranaroussi/quantstats)  -  Portfolio analytics for quants, written in Python.
- [skfolio](https://github.com/skfolio/skfolio)  -  Python library for portfolio optimization built on top of scikit-learn.
- [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib)  -  Portfolio Optimization and Quantitative Strategic Asset Allocation in Python.
- [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt)  -  Financial portfolio optimisation in Python, including classical efficient frontier, Black-Litterman, Hierarchical Risk Parity.
- [ffn](https://github.com/pmorissette/ffn)  -  ffn - a financial function library for Python.
- [pyfolio-reloaded](https://github.com/stefan-jansen/pyfolio-reloaded)  -  Portfolio and risk analytics in Python.
- [alphalens-reloaded](https://github.com/stefan-jansen/alphalens-reloaded)  -  Performance analysis of predictive (alpha) stock factors.
- [empyrical-reloaded](https://github.com/stefan-jansen/empyrical-reloaded)  -  Common financial risk and performance metrics. Used by zipline and pyfolio.

### Backtesting Data
#### Stock Data / TradFi Data
- [FirstRateData](https://firstratedata.com/)
- [Alpaca Data](https://alpaca.markets/data)
- [Polygon](https://polygon.io/)
#### Crypto Data
- [Bybit](https://public.bybit.com/trading/)
- [Bybit Spot](https://public.bybit.com/spot/)
- [Binance](https://www.binance.com/en/landing/data)
- [OKX](https://www.okx.com/data-download)
- [CCXT](https://docs.ccxt.com/#/)
#### DeFi Data
- [Trading Strategy](https://tradingstrategy.ai/trading-view)

### Live Trading Data
#### TradFi Data
- [Interactive Brokers](https://www.interactivebrokers.ca/en/pricing/market-data-pricing.php)
- [DTN IQFeed](https://www.dtn.com/refined-fuels/trader/iqfeed/)
- [Alpaca Data](https://alpaca.markets/data)

### Data Libraries
- [yfinance](https://github.com/ranaroussi/yfinance)  -  Download market data from Yahoo! Finance's API
- [binance-public-data](https://github.com/binance/binance-public-data)  -  Details on how to get Binance public data
- [pfeed](https://github.com/PFund-Software-Ltd/pfeed)  -  A Data Pipeline for Algo-Trading: Download -> Clean (ETL/ELT) -> Store Data. Supports Various Data Sources. Clean Once and Forget
- [FinanceDatabase](https://github.com/JerBouma/FinanceDatabase)  -  This is a database of 300.000+ symbols containing Equities, ETFs, Funds, Indices, Currencies, Cryptocurrencies and Money Markets

### Machine Learning Tools
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)  -  scikit-learn: machine learning in Python
- [pytorch](https://github.com/pytorch/pytorch)  -  Tensors and Dynamic neural networks in Python with strong GPU acceleration
- [pyro](https://github.com/pyro-ppl/pyro)  -  Deep universal probabilistic programming with Python and PyTorch


### Machine Learing Operations Tools
- [mlflow](https://github.com/mlflow/mlflow)  -  Open source platform for the machine learning lifecycle
- [feast](https://github.com/feast-dev/feast)  -  The Open Source Feature Store for Machine Learning
- [wandb](https://github.com/wandb/wandb)  -  The AI developer platform. Use Weights & Biases to train and fine-tune models, and manage models from experimentation to production.
- [dvc](https://github.com/iterative/dvc)  -   🦉 ML Experiments and Data Management with Git

### Data Tools
- [pandas](https://github.com/pandas-dev/pandas) – Flexible and powerful data analysis/manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more
- [polars](https://github.com/pola-rs/polars) – Dataframes powered by a multithreaded, vectorized query engine, written in Rust
- [spark](https://github.com/apache/spark) – Apache Spark - A unified analytics engine for large-scale data processing
- [dask](https://github.com/dask/dask) – Parallel computing with task scheduling
- [modin](https://github.com/modin-project/modin) – Modin: Scale your Pandas workflows by changing a single line of code
- [duckdb](https://github.com/duckdb/duckdb) – DuckDB is an analytical in-process SQL database management system
- [vaex](https://github.com/vaexio/vaex) – Out-of-Core hybrid Apache Arrow/NumPy DataFrame for Python, ML, visualization, and exploration of big tabular data at a billion rows per second 🚀
- [fugue](https://github.com/fugue-project/fugue) – A unified interface for distributed computing. Fugue executes SQL, Python, Pandas, and Polars code on Spark, Dask, and Ray without any rewrites
- [ibis](https://github.com/ibis-project/ibis) – The portable Python dataframe library
- [Daft](https://github.com/Eventual-Inc/Daft) – Distributed DataFrame for Python designed for the cloud, powered by Rust

### Research Tools
- [Quadratic](https://github.com/quadratichq/quadratic) – Quadratic | Spreadsheet with Python, SQL, and AI
- [OpenBBTerminal](https://github.com/OpenBB-finance/OpenBBTerminal) – Investment Research for Everyone, Everywhere
- [qlib](https://github.com/microsoft/qlib) – Qlib is an AI-oriented quantitative investment platform that aims to realize the potential, empower research, and create value using AI technologies in quantitative investment, from exploring ideas to implementing productions. Qlib supports diverse machine learning modeling paradigms. including supervised learning, market dynamics modeling, and RL

### Dashboard Tools
- [Streamlit](https://github.com/streamlit/streamlit) – Streamlit — A faster way to build and share data apps
- [Gradio](https://github.com/gradio-app/gradio) – Build and share delightful machine learning apps, all in Python. 🌟 Star to support our work!
- [Dash](https://github.com/plotly/dash) – Data Apps & Dashboards for Python. No JavaScript Required
- [Panel](https://github.com/holoviz/panel) – Panel: The powerful data exploration & web app framework for Python
- [Taipy](https://github.com/AxeldeRomblay/taipy) – Turns Data and AI algorithms into production-ready web applications in no time

### GPU Providers
#### Notebook-based
-  [Colab](https://colab.research.google.com/)
- [Deepnote](https://deepnote.com/)
- [Kaggle](https://www.kaggle.com/)
- [Lightning.ai](https://lightning.ai/)
#### Cloud-based
- [Vast.ai](https://vast.ai/)  -  Vast.ai is the market leader in low-cost cloud GPU rental. Use one simple interface to save 5-6X on GPU compute.
- [Lambda Labs](https://lambdalabs.com/)  -  The GPU Cloud for AI, On-demand & reserved cloud NVIDIA GPUs for AI training & inference
- [Paperspace](https://www.paperspace.com/)  -  Build & Run AI/ML Models on NVIDIA H100 GPUs, Develop, train, and deploy AI applications. Join over 500,000 builders on Paperspace.
- [Hyperstack](https://www.hyperstack.cloud/)  -  A Supercloud Specialised for AI
- [Datacrunch.io](https://datacrunch.io/)  -  The ML Cloud, Premium dedicated GPU servers and clusters, Model inference services
- [Nimbix](https://www.nimbix.net/)  -  On-demand access to GPU and CPU compute accelerators now and at scale.
- [TensorDock](https://tensordock.com/)  -  We make the GPU servers that cost too much on other clouds available for a low, hourly price.
- [Saturn Cloud](https://www.saturncloud.io/)  -  Saturn Cloud provides customizable, ready-to-use cloud environments for collaborative data teams. Run analyses, train models, deploy APIs, and more

### API Integrations/Connectors
#### Traditional Brokers
- [ibkr-docker](https://github.com/extrange/ibkr-docker)  - Run IBKR Gateway/TWS in a Docker container
- [ib_insync](https://github.com/erdewit/ib_insync)  - Python sync/async framework for Interactive Brokers API
- [alpaca-py](https://github.com/alpacahq/alpaca-py)  - The Official Python SDK for Alpaca API
#### Cryptocurrency Exchanges
- [CCXT](https://github.com/ccxt/ccxt)  -  A JavaScript / TypeScript / Python / C# / PHP cryptocurrency trading API with support for more than 100 bitcoin/altcoin exchanges
- [binance-connector-python](https://github.com/binance/binance-connector-python)  -  a simple connector to Binance Public API
- [pybit](https://github.com/bybit-exchange/pybit)  -  Official Python3 API connector for Bybit's HTTP and WebSockets APIs.
- [python-binance](https://github.com/sammchardy/python-binance)  -  Binance Exchange API python implementation for automated trading
- [tda-api](https://github.com/alexgolec/tda-api)  -  A TD Ameritrade API client for Python.
#### DeFi Exchanges
- [dydx-v3-python](https://github.com/dydxprotocol/dydx-v3-python)  -  Python client for dYdX (API v3)

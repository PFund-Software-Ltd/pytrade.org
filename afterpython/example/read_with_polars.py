# /// script
# dependencies = [
#     "marimo==0.25.2",
#     "pfeed[bybit]==0.0.24",
#     "polars==2.1.0",
# ]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    title: Read pfeed data with polars
    description: Download Bybit bars with pfeed, then query the stored parquet files directly with polars.
    tags: [pfeed, polars, parquet, bybit]
    date: 2026-11-11
    thumbnail: ./static/featured_thumbnail.png
    molab_badge: true
    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > Built with [pfeed →](https://pfeed.pfund.ai), an open-source data library by PFund,
    > which also maintains PyTrade.org.
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pfeed as pe
    import polars as pl

    return mo, pe, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Download data with pfeed
    Download one day of 1-minute ETH perpetual bars from Bybit, and store them
    locally with `ParquetIO()`.
    """)
    return


@app.cell
def _(pe):
    feed = pe.Bybit().market_feed
    df = feed.download(
        product="ETH_USDT_PERP",
        resolution="1m",
        start_date="2026-11-10",
        end_date="2026-11-10",
        io=pe.ParquetIO(),
    ).data.collect()
    df
    return (df,)


@app.cell
def _(pe):
    data_path = pe.get_config().data_path
    return (data_path,)


@app.cell(hide_code=True)
def _(data_path, df, mo):
    file_path = next(
        (data_path / "parquet").glob("**/product=BYBIT_ETH_USDT_PERPETUAL/**/*.parquet")
    ).relative_to(data_path / "parquet")
    tree = "\n".join(
        ("    " * (i - 1) + "└── " if i else "") + part
        for i, part in enumerate(file_path.parts)
    )
    mo.md(f"""
    ## Read it back with polars
    `ParquetIO()` stored the {df.height} rows as a plain parquet file in a hive layout
    under `<data_path>/parquet`, where `data_path` is pfeed's configured data folder:

    ```
    {tree.replace(chr(10), chr(10) + "    ")}
    ```

    So polars can read them directly. With `hive_partitioning=True`, every `key=value`
    folder becomes a column, and filtering on those columns only reads the matching files.
    """)
    return


@app.cell
def _(data_path, pl):
    polars_df = (
        pl.scan_parquet(
            data_path / "parquet" / "**" / "*.parquet", hive_partitioning=True
        )
        .filter(
            pl.col("data_source") == "BYBIT",
            pl.col("product") == "BYBIT_ETH_USDT_PERPETUAL",
            pl.col("resolution") == "1_MINUTE",
        )
        .select("date", "open", "high", "low", "close", "volume")
        .collect()
    )
    polars_df
    return


if __name__ == "__main__":
    app.run()

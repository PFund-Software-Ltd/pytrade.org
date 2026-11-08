# /// script
# requires-python = ">=3.13"
# dependencies = ["marimo==0.25.2", "pytrade", "httpx2==2.16.0", "python-dotenv==1.2.4"]
#
# [tool.uv.sources]
# pytrade = { path = "../../../..", editable = true }
# ///
import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Verdicts
    """)
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    print('⚖️')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    (ai-hedge-fund-verdict)=
      ## AI Hedge Fund
      *version xxxx*

    - test1
    - test2
    """)
    return


if __name__ == "__main__":
    app.run()

from collections.abc import Iterable
from typing import Any


def html_table(
    headers: Iterable[Any],
    rows: Iterable[Iterable[Any]],
    use_ipython: bool = True,
) -> Any:
    """Build a minimal HTML ``<table>`` from headers and rows.

    The markup is unstyled so it inherits the site theme's table styling
    (myst strips injected ``<style>`` blocks and class attributes from cell
    output anyway). Cell values are emitted as-is, so callers may pass HTML
    (e.g. ``<a href=...>`` links, ``<strong>`` text) directly.

    When ``use_ipython`` is true (the default), the result is wrapped in
    ``IPython.display.HTML`` so a notebook cell renders it as a table and
    MyST-NB emits it verbatim into the built site. Set it to ``False`` to
    get the raw HTML string instead.
    """
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
        for row in rows
    )
    table = f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"

    if use_ipython:
        from IPython.display import HTML

        return HTML(table)
    return table

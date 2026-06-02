"""Render a table of trading-framework repos with live GitHub stats.

A page defines a ``REPOS`` dict (see ``algo_trading``/``ai_trading``) mapping a
repo key to ``{"github": "owner/name", <capability fields...>}`` and calls
``repos_table(REPOS)`` in a notebook cell to render the table.
"""

import os
from typing import Any

import niquests
from dotenv import load_dotenv

from pytrade.utils import html_table

# GitHub result columns, in order, appended after the user-defined fields.
GITHUB_HEADERS = ["Stars", "Issues", "Contributors", "Version", "Last Publish"]

# Tri-state capability symbols: True -> YES, False -> NO, None -> N/A
# (e.g. a market-agnostic library where the column doesn't apply).
YES = "✔️"
NO = "✖️"
NA = "➖"

# header -> tooltip; the {abbr} role can't run inside raw-HTML output, so we
# emit the equivalent <abbr title="..."> tag directly.
HEADER_ABBR = {
    "Live": "Live Trading",
    "ML-Native": "Machine Learning Native",
    "Approach": "How the project creates trading decisions",
}


def _get(url: str) -> Any:
    """GET a GitHub API URL and return parsed JSON, raising a clear error.

    The API returns a JSON object (not the expected repo/list) on failures
    like rate limiting — surface that message instead of a cryptic KeyError.
    """
    load_dotenv(override=True)
    resp = niquests.get(
        url,
        headers=(
            {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
            if os.environ.get("GITHUB_TOKEN")
            else {}
        ),
    )
    data = resp.json()
    if resp.status_code != 200:
        message = data.get("message", data) if isinstance(data, dict) else data
        raise RuntimeError(f"GitHub API {resp.status_code} for {url}: {message}")
    return data


def _fetch_repo(github: str) -> dict:
    repo = _get(f"https://api.github.com/repos/{github}")
    contributors = _get(f"https://api.github.com/repos/{github}/contributors")
    releases = _get(f"https://api.github.com/repos/{github}/releases")

    # contributors/releases are lists; guard in case the API returns otherwise
    contributors = contributors if isinstance(contributors, list) else []
    releases = releases if isinstance(releases, list) else []
    latest = releases[0] if releases else {}
    published_at = latest.get("published_at") or ""
    return {
        "name": repo["name"],
        "full_name": repo["full_name"],
        "stars": repo["stargazers_count"],
        # open_issues includes open PRs — matches the old table's behaviour
        "issues": repo["open_issues"],
        "contributors": len(contributors),
        "version": latest.get("name") or "",
        # keep date only, drop the time component
        "last_publish": published_at[:10],
    }


def _render_header(name: str) -> str:
    full = HEADER_ABBR.get(name)
    return f'<abbr title="{full}">{name}</abbr>' if full else name


def _render_field(field: str, value: Any) -> str:
    """Render a capability/text cell.

    Tri-state: ``True`` -> YES (✔️), ``False`` -> NO (✗), ``None`` -> N/A (—,
    e.g. a market-agnostic library). Other fields render as text, with Status
    bolded because it's the most important column.
    """
    if value is None:
        return NA
    if isinstance(value, bool):
        return YES if value else NO
    text = str(value)
    return f"<strong>{text}</strong>" if field == "Status" else text


def repos_table(repos: dict, use_ipython: bool = True) -> Any:
    """Build the repos table: Repo, the user-defined fields, then GitHub stats."""
    # user-defined columns are every REPOS field except the github slug, in order
    field_keys: list[str] = []
    for info in repos.values():
        for key in info:
            if key.lower() != "github" and not key.startswith("_") and key not in field_keys:
                field_keys.append(key)

    headers = [_render_header(h) for h in ["Repo", *field_keys, *GITHUB_HEADERS]]

    rows = []
    for info in repos.values():
        github = info["github"]
        if info.get("_fetch_github", True):
            d = _fetch_repo(github)
        else:
            d = {
                "name": github.split("/")[-1],
                "full_name": github,
                "stars": None,
                "issues": None,
                "contributors": None,
                "version": "",
                "last_publish": "",
            }
        url = f"https://github.com/{d['full_name']}"
        row = [f'<a href="{url}">{d["name"]}</a>']
        row += [_render_field(field, info.get(field)) for field in field_keys]
        row += [
            f"<strong>{d['stars']:,}</strong>" if d["stars"] is not None else NA,
            d["issues"] if d["issues"] is not None else NA,
            d["contributors"] if d["contributors"] is not None else NA,
            d["version"] or NA,
            d["last_publish"] or NA,
        ]
        rows.append(row)

    return html_table(headers, rows, use_ipython=use_ipython)

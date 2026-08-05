"""Resolve the latest Pyodide release that bundles a given Python version.

Usage:
    python3 resolve_pyodide_version.py <python_version>

<python_version> may be a full version (e.g. "3.11.3") or just
major.minor (e.g. "3.11"), in which case the latest matching patch
release is used.

Prints the resolved Pyodide version (e.g. "0.25.1") to stdout, or exits
with a non-zero status and an error message on stderr if no matching
release is found.
"""

import json
import re
import sys
import urllib.request

RELEASES_URL = (
    "https://pyodide.github.io/pyodide/api/v2/pyodide-cross-build-environments.json"
)
STABLE_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")


def version_key(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split("."))


def resolve_pyodide_version(python_version: str) -> str:
    with urllib.request.urlopen(RELEASES_URL) as response:
        data = json.load(response)

    matches = [
        release
        for release in data["releases"].values()
        if STABLE_VERSION_RE.match(release["version"])
        and (
            release["python_version"] == python_version
            or release["python_version"].startswith(python_version + ".")
        )
    ]

    if not matches:
        raise SystemExit(
            f"Could not find a Pyodide release matching Python version "
            f"'{python_version}'"
        )

    latest = max(matches, key=lambda release: version_key(release["version"]))
    return latest["version"]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"Usage: {sys.argv[0]} <python_version>")

    print(resolve_pyodide_version(sys.argv[1]))

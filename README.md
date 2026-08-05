# pyodide-actions

Github Actions snippets for Pyodide

## Usage

### `install-browser`

```yaml
...
steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - uses: pyodide/pyodide-actions/install-browser
      with:
        runner: selenium
        browser: chrome
        browser-version: latest
```

#### Inputs

- `runner` -  `selenium` or `plawright`
- `browser` - `chrome` or `firefox` or `node` or `safari`
- `browser-version` - browser version, e.g. `latest` (chrome) or `18` (node)
- `driver-version` - webdriver version, only for `selenium` runner
- `playwright-version` - specify playwright version, only for `playwright` runner
- `python-executable` - path to python executable, default is `python`


### `download-pyodide`

```yaml
...
steps:
    - uses: actions/checkout@v3
    - uses: pyodide/pyodide-actions/download-pyodide
      with:
        version: 0.21.0
        to: dist
```

You can also pick the latest Pyodide release that bundles a given Python
version, instead of specifying an exact Pyodide version:

```yaml
...
steps:
    - uses: actions/checkout@v3
    - uses: pyodide/pyodide-actions/download-pyodide
      with:
        python_version: "3.11"
        to: dist
```

### Inputs

- `version` - Pyodide version, e.g. `0.21.0`. Mutually exclusive with `python_version`.
- `python_version` - Python version bundled by Pyodide, e.g. `3.11` or `3.11.3`. Resolves to the latest matching Pyodide release. Mutually exclusive with `version`.
- `to` - path to download Pyodide

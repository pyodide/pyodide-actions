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

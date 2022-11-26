import shutil
import importlib.util

def exists(executables: list[str]) -> bool:
    return all([shutil.which(exe) is not None for exe in executables])

# TODO: more robust way to check if a browser is installed
if exists(["google-chrome", "chromedriver"]):
    print("[*] selenium/chrome found")
if exists(["firefox", "geckodriver"]):
    print("[*] selenium/firefox found")
if exists(["node"]):
    print("[*] selenium/node found")
if exists(["safaridriver"]):
    print("[*] selenium/safari found")
if importlib.util.find_spec("playwright") is not None:
    print("[*] playwright/chrome found")
    print("[*] playwright/firefox found")

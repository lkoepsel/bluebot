# BlueBot Charting App

## Installation
```bash
mkdir bluebot
cd bluebot
uv init
uv venv 
source .venv/bin/activate
uv pip install pandas matplotlib
uv chart_bb.py

# once through with app
deactivate
```

## Usage
Use to chart BlueBot data from Pump. To download data:
[Bluebot Flow Dash](https://dashboard.bluebot.com/data-export/)

1. Specify specific bluebot data desired
2. Specify date range
3. Download
4. 
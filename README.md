<h1 align="center">Python TradingView TA by Analyzer.REST</h1>
<div align="center">
  <img src="https://img.shields.io/readthedocs/python-tradingview-ta/latest?style=for-the-badge" />
  <img src="https://img.shields.io/github/license/nazguul512/python-tradingview-ta-v3?style=for-the-badge" />
  <img src="https://img.shields.io/pypi/v/tradingview-ta-v3?style=for-the-badge" />
</div>
<br>
<div align="center">
  <p>An unofficial API wrapper for TradingView that allows you to fetch technical analysis data, now under new management.</p>
  <h3>Brought to you by Analyzer.REST and nazguul512 which provides Technical Analysis-as-a-Service (TAaaS) through an intuitive and affordable API.</h3>
  <img src="https://raw.githubusercontent.com/nazguul512/python-tradingview-ta-v3/main/images/tradingview.png" />
</div>

## Important
 - Keep tradingview-ta-v3 up to date for new features and bug fixes: `pip install -U tradingview_ta_v3`
 - Technical analysis for indices (index) is not supported by both TradingView and tradingview-ta_v3.
 
## Features
* Faster response (older version of tradingview-ta requires Selenium)
* [Support for multiple symbols](https://python-tradingview-ta.readthedocs.io/en/latest/usage.html#retrieving-multiple-analysis)
* Indicators (Only TradingView built-in, does not support Pine Script/custom indicators)


## Requirements
 - Python 3.8 or newer.
 - [Requests](https://pypi.org/project/requests/), included in installation.
 
## Installation
 [PyPI](https://pypi.org/project/tradingview-ta-v3/) (stable, recommended):
 
```pip install tradingview_ta```

 GitHub (latest):
 
```pip install git+https://github.com/nazguul512/python-tradingview-ta-v3.git```


## Example
```python
from tradingview_ta_v3 import TA_Handler, Interval, Exchange

tesla = TA_Handler(
    symbol="TSLA",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_DAY,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)
print(tesla.get_analysis().summary)
# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}
```

Tip: Use https://tvdb.analyzer.rest/ if you don't know what symbol, screener, and exchange to use.

## Documentation
 [Read The Docs](https://python-tradingview-ta.readthedocs.io)

## Issue
 If you found a bug or have a question, please open an issue. Email will not be replied.
  
## Warning
 Trading is a risky activity, especially when done using an automated program. Never trade automatically without your supervision using results provided by tradingview-ta. Any monetary losses are not my fault.

## Contributing
 Pull requests (docs, bug fix, features) are welcomed! Any pull request (documentation, bug fix, features, etc) are welcomed. Please follow the [guidelines](https://github.com/nazguul512/python-tradingview-ta-v3/blob/main/CONTRIBUTING.md) and the [code of conduct](https://github.com/nazguul512/python-tradingview-ta-v3/blob/main/CODE_OF_CONDUCT.md).
 
## License
 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

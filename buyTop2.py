from tda.orders.common import OrderType
from tda.orders.generic import OrderBuilder

import requests

import os, sys
from tda import auth, client
from tda.orders.equities import equity_buy_market, equity_buy_limit
from tda.orders.common import Duration, Session
import tda

# currentdir = os.path.dirname(os.path.realpath(__file__))
currentdir = os.path.abspath('')
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import config

from selenium import webdriver
import time
import json

# import my_templates

def trailTrailBuy (ticker, quantity):
    order_template = {
    "orderStrategyType": "TRIGGER",
    "orderType": "TRAILING_STOP",
    "stopPriceOffset": 3, 
    "stopPriceLinkType": "PERCENT",
    "stopPriceLinkBasis": "BID",
    "stopType": "STANDARD",
    "session": "NORMAL",
    "duration": "GOOD_TILL_CANCEL",
    "orderStrategyType": "SINGLE",
    "orderLegCollection": [
        {
            "instruction": "BUY",
            "quantity": quantity,
            "instrument": {
                "symbol": ticker,
                "assetType": "EQUITY"
            }
        }
    ],
    #These are the child orders, these will take effect when the buy order is filled.
    "childOrderStrategies": [
    {
    "orderType": "TRAILING_STOP",
    "stopPriceOffset": 10, 
    "stopPriceLinkType": "PERCENT",
    "stopPriceLinkBasis": "BID",
    "stopType": "STANDARD",
    "session": "NORMAL",
    "duration": "GOOD_TILL_CANCEL",
    "orderStrategyType": "SINGLE",
    "orderLegCollection": [
        {
            "instruction": "SELL",
            "quantity": quantity,
            "instrument": {
                "symbol": ticker,
                "assetType": "EQUITY"
            }
        }
    ]
    }
    ]
    }
    return order_template

token_path = "token"

DRIVER_PATH = "/home/hopper/chromedriver"
driver = webdriver.Chrome(DRIVER_PATH)

redirect_uri = "https://localhost"

try:
    c = auth.client_from_token_file(token_path, config.api_key)
except FileNotFoundError:
    c = auth.client_from_login_flow(driver, config.api_key, redirect_uri, token_path)

driver.get("https://financhill.com/screen/stock-score")
time.sleep(2)
print('1.1')
# driver.find_element_by_css_selector(
#     'span[data-sort-name="stock_score_normalized"]'
# ).click()
time.sleep(10)
print('1.2')
tickers = driver.find_elements_by_tag_name("td")

positions = c.Account.Fields.POSITIONS
r = c.get_account(config.tda_acct_num, fields=positions)
stocks = r.json()['securitiesAccount']['positions']

stock_symbols = [] #append later

for stock in stocks:
    stock_symbols.append(stock['instrument']['symbol'])

new_stocks_found = False

already_owned = []
advanced_mode = True
i = 0
bought = 0
# [0]:Ticker, [1]:Share Price, [2]:Rating, [3]:Score, [4]:Rating Change Date, [5]:Price Change %
# Check the top 20 stocks on Financhill

# c.place_order(config.tda_acct_num, trailTrailBuy('SNDL', 2))
# driver.quit()
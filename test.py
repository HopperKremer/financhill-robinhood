#jul 6 2021
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

token_path = "token"

DRIVER_PATH = "/home/hopper/chromedriver"

# sys.setProperty("webdriver.chrome.driver", "C:\\path\\to\\chromedriver.exe");
options = webdriver.ChromeOptions()
# options.addArguments("start-maximized"); # open Browser in maximized mode
# options.addArguments("disable-infobars"); # disabling infobars
# options.addArguments("--disable-extensions"); # disabling extensions
# options.addArguments("--disable-dev-shm-usage"); # overcome limited resource problems
options.add_argument("--no-sandbox") # Bypass OS security model

driver = webdriver.Chrome(DRIVER_PATH, options=options)
# driver = webdriver.Chrome(DRIVER_PATH)

redirect_uri = "https://localhost"

try:
    c = auth.client_from_token_file(token_path, config.api_key)
except FileNotFoundError:
    c = auth.client_from_login_flow(driver, config.api_key, redirect_uri, token_path)

# r = c.get_order(3983169830, config.tda_acct_num)

# print(r)
# print(r.json())

positions = c.Account.Fields.POSITIONS
r = c.get_account(config.tda_acct_num, fields=positions)

stocks = r.json()['securitiesAccount']['positions']

stock_symbols = [] #append later

for stock in stocks:
    # break
    ticker = stock['instrument']['symbol']
    if ticker == 'MMDA1':
        continue
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get("https://financhill.com/search/stock-score/" + ticker)
    time.sleep(2)

    score = int(driver.find_element_by_tag_name("h2").text)
    print(ticker + ", rated " + str(score) + ", day p/l = " + str(stock['currentDayProfitLoss']))

    # if (score < 40):
    #     r.order_sell_trailing_stop(stock, data['quantity'], 1)
    #     soldStocks.append(stock)

    driver.quit()

# APT, rated 88, day p/l = -74.42
# BIDU, rated 89, day p/l = 17.73
# RJA, rated 85, day p/l = 4.32
# AMSWA, rated 79, day p/l = 7.2
# XNET, rated 84, day p/l = 15.73
# LOCO, rated 88, day p/l = -4.9
# APEI, rated 86, day p/l = 8.96
# MRNS, rated 94, day p/l = 91.43
# PFF, rated 40, day p/l = -3.3
# GDDY, rated 83, day p/l = -59.07
# MPX, rated 76, day p/l = 66.01
# RENN, rated 85, day p/l = 100.44
# GME, rated 50, day p/l = 17.2
# CHIC, rated 98, day p/l = 9.9
# AB, rated 82, day p/l = -27.04
# NBSE, rated 77, day p/l = 45.36
# CVLT, rated 88, day p/l = 3.75
# VTWG, rated 86, day p/l = 1.08
# KWEB, rated 89, day p/l = 5.4
# CMRX, rated 75, day p/l = 12.48
# AR, rated 78, day p/l = 135.3




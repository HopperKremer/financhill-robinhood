# from excel import OpenExcel
import requests
from tda import auth, client
from tda.orders.equities import equity_buy_market
from tda.orders.common import Duration, Session
import os, sys
import time


currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import config

from selenium import webdriver

import json

DRIVER_PATH = "/home/hopper/chromedriver"
driver = webdriver.Chrome(DRIVER_PATH)

redirect_uri = "https://localhost"

try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    c = auth.client_from_login_flow(
        driver, config.api_key, redirect_uri, config.token_path
    )

driver.get("https://financhill.com/screen/stock-score")
time.sleep(2)

driver.find_element_by_css_selector(
    'span[data-sort-name="stock_score_normalized"]'
).click()

time.sleep(2)

tickers = driver.find_elements_by_tag_name("td")

i = 0
while i < 10:
    ticker = tickers[i].text
    print(ticker)
    url = "https://api.tdameritrade.com/v1/accounts/" + con + "/orders"

    # response = c.place_order(
    # config.tda_acct_num,  # account_id
    # equity_buy_market(str(tickers[i].text), 1)
    #     .set_duration(Duration.GOOD_TILL_CANCEL)
    #     .set_session(Session.SEAMLESS)
    #     .build())
    # print(response)
    # print(response.status_code)
    i+=10
# time.sleep(2)

driver.quit()

# [0]: Ticker, [1]: Price, [2]: Rating, [3]: Score, [4]:Rating Change Date, [5]:Price Change %
# SVM
# 6.70
# Buy
# 92
# 2021-01-29
# 9.48%
# CHART



# REGI
# 94.57
# Buy
# 92
# 2020-12-11
# 63.47%
# CHART



# WISH
# 29.35
# Buy
# 91
# 2021-01-08
# 40.23%
# CHART



# AGQ
# 50.12
# Buy
# 89
# 2020-12-01
# 32.31%
# CHART
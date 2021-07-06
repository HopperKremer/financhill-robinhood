# Buy top tickers from Financhill
import requests
from tda import auth, client
from tda.orders.equities import equity_buy_market
from tda.orders.common import Duration, Session
import tda
import os, sys
import time

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)
import config  # stored in parent directory for security

from selenium import webdriver

import json

token_path = 'token'

DRIVER_PATH = "/home/hopper/chromedriver"
driver = webdriver.Chrome(DRIVER_PATH)

redirect_uri = "https://localhost"

try:
    c = auth.client_from_token_file(token_path, config.api_key)
except FileNotFoundError:
    c = auth.client_from_login_flow(
        driver, config.api_key, redirect_uri, token_path
    )
#All this scraping code works
driver.get("https://financhill.com/screen/stock-score")
time.sleep(2)
driver.find_element_by_css_selector(
    'span[data-sort-name="stock_score_normalized"]'
).click()
time.sleep(2)
tickers = driver.find_elements_by_tag_name("td")

i = 0
# this will only loop once as a test
while i < 10:
    # ticker = str(tickers[i].text)
    # print(ticker)
    # print(c.place_order(
    #     config.tda_acct_num,  # account_id
    #     equity_buy_market(ticker, 1)
    #     .set_duration(Duration.GOOD_TILL_CANCEL)
    #     .set_session(Session.SEAMLESS)
    #     .build()
    # ))
    # time.sleep(2)
    # i += 10
    ticker = str(tickers[i].text)
    print(ticker)
    order = tda.orders.equities.equity_buy_market(ticker, 1)
    r = c.place_order(config.tda_acct_num, order)
    time.sleep(2)
    print(r.status_code)
    i += 10
driver.quit()
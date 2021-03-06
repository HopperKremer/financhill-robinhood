import requests
from tda import auth, client
from tda.orders.equities import equity_buy_market
from tda.orders.common import Duration, Session
import os, sys
import time
from selenium import webdriver
import json

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import config  # stored in parent directory for security

token_path = 'token'
redirect_uri = "https://localhost"

DRIVER_PATH = "/home/hopper/chromedriver"
driver = webdriver.Chrome(DRIVER_PATH)


try:
    c = auth.client_from_token_file(token_path, config.api_key)
except FileNotFoundError:
    c = auth.client_from_login_flow(
        driver, config.api_key, redirect_uri, token_path
    )

i = 0
# this will only loop once as a test
while i < 10:
    ticker = str(tickers[i].text)
    print(ticker)
    print(c.place_order(
        config.tda_acct_num,  # account_id
        equity_buy_market(ticker, 1)
        .set_duration(Duration.GOOD_TILL_CANCEL)
        .set_session(Session.SEAMLESS)
        .build()
    ))
    time.sleep(2)
    i += 10
driver.quit()
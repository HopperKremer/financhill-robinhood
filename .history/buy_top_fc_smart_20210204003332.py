# Buy top tickers from Financhill
import requests
from tda import auth, client
from tda.orders.equities import equity_buy_market, equity_buy_limit
from tda.orders.common import Duration, Session
import tda
import os, sys
import time
from selenium import webdriver
import json

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)
import config  # stored in parent directory for security


token_path = "token"

DRIVER_PATH = "/home/hopper/chromedriver"
driver = webdriver.Chrome(DRIVER_PATH)

redirect_uri = "https://localhost"

try:
    c = auth.client_from_token_file(token_path, config.api_key)
except FileNotFoundError:
    c = auth.client_from_login_flow(driver, config.api_key, redirect_uri, token_path)
# All this scraping code works
driver.get("https://financhill.com/screen/stock-score")
time.sleep(2)
driver.find_element_by_css_selector(
    'span[data-sort-name="stock_score_normalized"]'
).click()
time.sleep(2)
tickers = driver.find_elements_by_tag_name("td")



positions = c.get_account(config.tda_acct_num, c.Account.Fields.POSITIONS)
print(positions)

i = 0
# [0]:Ticker, [1]:Share Price, [2]:Rating, [3]:Score, [4]:Rating Change Date, [5]:Price Change %
while i < 40:
    ticker = str(tickers[i].text)
    print(ticker)

    share_price = float(tickers[i + 1].text)

    desired_dollar_amount = 1000 # How many dollars of each stock to buy
    num_shares = round(desired_dollar_amount / share_price)
    print(num_shares)

    order = equity_buy_market(ticker, num_shares)
    r = c.place_order(config.tda_acct_num, order)
    time.sleep(2)
    print(r.status_code)
    print("Bought " )
    i += 10

driver.quit()
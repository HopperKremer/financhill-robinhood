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



# positions = c.get_account(config.tda_acct_num, c.Account.Fields.POSITIONS)
# print(positions)

i = 60
# [0]:Ticker, [1]:Share Price, [2]:Rating, [3]:Score, [4]:Rating Change Date, [5]:Price Change %
while i < 100:
    # Get ticker and price of stock
    ticker = str(tickers[i].text)
    share_price = float(tickers[i + 1].text)
    # Calculate how many shares to buy in order to equal about $1000
    desired_dollar_amount = 1000 # How many dollars of each stock to buy
    num_shares = round(desired_dollar_amount / share_price)
    #Build and place order
    order = equity_buy_market(ticker, num_shares)
    r = c.place_order(config.tda_acct_num, order)
    print("Bought " + str(num_shares) + " of " + ticker)
    i += 10

driver.quit()


# Better way to write?:
# i = 0
# while i < 6:
#     ticker = str(tickers[i*10].text)
#     share_price = float(tickers[i*10 + 1].text)
#     i+=1
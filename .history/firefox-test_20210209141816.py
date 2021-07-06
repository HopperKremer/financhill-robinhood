print("hi")
import requests
import os, sys
from tda import auth, client
from tda.orders.equities import equity_buy_market, equity_buy_limit
from tda.orders.common import Duration, Session
import tda
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://financhill.com/search/stock-score/" + stock)

# browser = webdriver.Firefox()
# browser.get('https://financhill.com/')
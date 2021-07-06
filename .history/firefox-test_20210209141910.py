print("hi")
import requests
import os, sys
from tda import auth, client
from tda.orders.equities import equity_buy_market, equity_buy_limit
from tda.orders.common import Duration, Session
import tda
from selenium import webdriver

driver = webdriver.Firefox(executable_path="/home/hopper/geckodriver")
driver.get("https://financhill.com/search/stock-score/" )

# browser = webdriver.Firefox()
# browser.get('https://financhill.com/')
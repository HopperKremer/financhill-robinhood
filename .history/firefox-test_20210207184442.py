print("hi")
import requests
import os, sys
from tda import auth, client
from tda.orders.equities import equity_buy_market, equity_buy_limit
from tda.orders.common import Duration, Session
import tda

browser = webdriver.Firefox()
browser.
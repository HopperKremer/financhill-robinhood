# from excel import OpenExcel
from tda import auth, client
import os, sys

# currentdir = os.path.dirname(os.path.realpath(__file__))
currentdir = os.path.abspath('')
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import config

from tda.orders.equities import equity_sell_market

from selenium import webdriver

import json

DRIVER_PATH = "/home/hopper/chromedriver"
driver = webdriver.Chrome(DRIVER_PATH)

redirect_uri = "https://localhost"
try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    # with webdriver.Chrome() as driver:
    c = auth.client_from_login_flow(
        driver, config.api_key, redirect_uri, config.token_path
    )

order = equity_sell_market('LEAF', 1).set_order_type(tda.OrderType.TRAILING_STOP).set_stop_price_link_type(PriceLinkType.PERCENT).set_stop_price_offset(1)

c.place_order(config.tda_accta_num, order)
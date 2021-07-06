import requests
from tda import auth, client
from tda.orders.equities import EquityOrderBuilder
# from tda.orders import EquityOrderBuilder
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
time.sleep(2)


# print(c.place_order(config.tda_acct_num, equity_buy_market('SNDL', 1).set_duration(Duration.GOOD_TILL_CANCEL).set_session(Session.SEAMLESS).build()))

builder = EquityOrderBuilder('SNDL', 1)
builder.set_instruction(EquityOrderBuilder.instruction.BUY)
builder.set_order_type(EquityOrderBuilder.OrderType.MARKET)
builder.set_duration(Duration.DAY)
builder.set_session(Session.NORMAL)

response = c.place_order(config.tda_acct_num, builder.build())

print(response)

time.sleep(2)
driver.quit()
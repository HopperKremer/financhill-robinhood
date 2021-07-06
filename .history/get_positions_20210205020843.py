# Buy top tickers from Financhill
import requests
from tda import auth, client
from tda.orders.equities import equity_buy_market, equity_buy_limit
from tda.orders.common import Duration, Session
import os, sys
import time
from selenium import webdriver
import json

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)
import config  # stored in parent directory for security


token_path = "token"

c = auth.client_from_token_file(token_path, config.api_key)

# positions = c.get_account(config.tda_acct_num, c.Account.Fields.POSITIONS)
# account_info = c.get_account(config.tda_acct_num, fields=[c.Account.Fields.POSITIONS]).json()
# print(account_info)

# positions = c.Account.Fields.POSITIONS
# r = c.get_account(config.tda_acct_num, fields=positions)

# stocks = r.json()['securitiesAccount']['positions']
# # stocks = json.dumps(r.json(), indent=4)

# for stock in stocks:
#     print('--------------------------------')
#     print(stock['instrument']['symbol'])
orders = c.Order.Status.FILLED


# res = c.get_orders_by_path(config.tda_acct_num, status = orders)
res = s = c.get_account(config.account_id, fields=c.Account.Fields.POSITIONS)
data = res.json()
print(data)
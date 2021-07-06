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


# orders = c.Order.Status.FILLED

# r = c.get_orders_by_path(config.tda_acct_num, status = client.Client.Order.Status.WORKING)

# res = c.get_orders_by_path(config.tda_acct_num, status = orders)
# res = s = c.get_account(config.tda_acct_num, fields=c.Account.Fields.POSITIONS)
# data = r.json()
# print(r.json())




orders = client.Client.Account.Fields.ORDERS
r = c.get_account(config.tda_acct_num, fields=orders)
print(json.dumps(r.json(), indent=4))#queued orders would  appear here, if not blank list
l = r.json()['securitiesAccount']['orderStrategies']
canceled_orders = [i['orderId'] for i in l if i['status'] == 'CANCELED']
print('canceled', canceled_orders)

ids_to_cancel = []

# for order_id in canceled_orders:
# g = c.get_order(order_id, config.tda_acct_num)
# print(json.dumps(g.json(), indent=4))

for order in r.json()['securitiesAccount']['orderStrategies']:
    print(order['orderId'])
    # order_id = int(order['orderId'])
    # print('Canceling order for ' + str(order['quantity']) + " shares of " + order['orderLegCollection']['instrument']['symbol'])
    # c.cancel_order(order_id, config.tda_acct_num)
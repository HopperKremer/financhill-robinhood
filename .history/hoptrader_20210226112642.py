# from excel import OpenExcel
from tda import auth, client
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import config

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

r = c.get_price_history(
    "AAPL",
    period_type=client.Client.PriceHistory.PeriodType.YEAR,
    period=client.Client.PriceHistory.Period.TWENTY_YEARS,
    frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
    frequency=client.Client.PriceHistory.Frequency.DAILY,
)
assert r.status_code == 200, r.raise_for_status()
print(json.dumps(r.json(), indent=4))






# order_template = {
#   #This is my buy order, this will trigger the other one.
#   "orderStrategyType": "TRIGGER",
#   "session": "NORMAL",
#   "orderType": "MARKET",
#   "duration": "DAY",
#   "orderLegCollection": [
#     {
#       "instruction": "BUY",
#       "quantity": 1,
#       "instrument": {
#         "assetType": "EQUITY",
#         "symbol": "LEAF"
#       }
#     }
#   ],
#   #These are the child orders, these will take effect when the buy order is filled.
#   "childOrderStrategies": [
#     {
#     "orderType": "TRAILING_STOP",
#     "stopPriceOffset": 2, 
#     "stopPriceLinkType": "PERCENT",
#     "stopPriceLinkBasis": "BID",
#     "stopType": "STANDARD",
#     "session": "NORMAL",
#     "duration": "GOOD_TILL_CANCEL",
#     "orderStrategyType": "SINGLE",
#       "orderLegCollection": [
#         {
#           "instruction": "SELL",
#           "quantity": 1,
#           "instrument": {
#             "assetType": "EQUITY",
#             "symbol": "LEAF"
#           }
#         }
#       ]
#     }
#   ]
# }  


# r = c.place_order(account_id, order_template)



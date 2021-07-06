import requests

import os, sys
from tda import auth, client
from tda.orders.equities import equity_buy_market, equity_buy_limit
from tda.orders.common import Duration, Session
import tda

currentdir = os.path.dirname(os.path.realpath(__file__))
# currentdir = os.path.abspath('')
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import config

from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "/home/hopper/chromedriver"

# Then when you authenticate. excecutable_path is where chromedriver is located on your system.
### AUTENTICATE ###
try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(chrome_options=options, executable_path= r'C:\Users\absco\Anaconda3\envs\td_ameritrade\chromedriver') as driver:
        c = auth.client_from_login_flow(
        driver, config.api_key, config.redirect_uri, config.token_path)






from selenium import webdriver
import time
import json

token_path = "token"

# DRIVER_PATH = "/home/hopper/chromedriver"
print("hi")
driver = webdriver.Chrome(DRIVER_PATH)

redirect_uri = "https://localhost"


PATH = "/home/hopper/chromedriver"
token_path = "token"

# try:
#     c = auth.client_from_token_file(token_path, config.api_key)
# except FileNotFoundError:
#     c = auth.client_from_login_flow(driver, config.api_key, redirect_uri, token_path)



# All this scraping code works
driver.get("https://financhill.com/screen/stock-score")
time.sleep(2)
print('1.1')
driver.find_element_by_css_selector(
    'span[data-sort-name="stock_score_normalized"]'
).click()
time.sleep(2)
print('1.2')
tickers = driver.find_elements_by_tag_name("td")

positions = c.Account.Fields.POSITIONS
r = c.get_account(config.tda_acct_num, fields=positions)
stocks = r.json()['securitiesAccount']['positions']

stock_symbols = [] #append later

for stock in stocks:
    stock_symbols.append([stock['instrument']['symbol'], stock['instrument']['symbol']])

new_stocks_found = False

already_owned = []
advanced_mode = True
i = 0
bought = 0
# [0]:Ticker, [1]:Share Price, [2]:Rating, [3]:Score, [4]:Rating Change Date, [5]:Price Change %
# Check the top 20 stocks on Financhill
while i < 20:

    # Get ticker and price of stock
    ticker = str(tickers[10*i].text)
    share_price = float(tickers[10*i + 1].text)

    # Calculate how many shares to buy in order to equal about $1000
    desired_dollar_amount = 1000 # How many dollars of each stock to buy
    num_shares = round(desired_dollar_amount / share_price)

    if bought >= 6:
        break
    # Skip if ticker is already owned
    elif (ticker in stock_symbols):
        already_owned.append(str(i) + '. You already own ' + ticker)
        i+=1
        if advanced_mode:
            shares_to_buy = int(input("You already own " + ticker + ", enter how many shares to buy(0 to skip):"))
            # Build, place, & print order (uncomment next 2 lines to buy)
            # order = equity_buy_market(ticker, shares_to_buy)
            # r = c.place_order(config.tda_acct_num, order)
            bought+=1
    else:
        # Build, place, & print order (uncomment next 2 lines to buy)
        # order = equity_buy_market(ticker, num_shares)
        # r = c.place_order(config.tda_acct_num, order)
        print(str(i) + ". Bought " + str(num_shares) + " shares of " + ticker + " up " + tickers[10*i + 5].text + " at $" + tickers[10*i + 1].text)
        bought += 1
        # Toggle message and increment counter
        new_stocks_found = True
        i += 1
for sentence in already_owned:
    print(sentence)

# If no new stocks were found
if (not new_stocks_found):
    print("You already own all the top stocks")

driver.quit()
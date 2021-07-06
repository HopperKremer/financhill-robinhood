# For Robinhood, see hoptrader.py for TD Ameritrade
# Cancel all pending sell orders before running if you want to apply to every stock
import os, sys
from tda import auth, client


currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import config
import holdings

from selenium import webdriver
import time

# totp = pyotp.TOTP("My2factorAppHere").now()
# login = r.login(config.USERNAME, config.PASSWORD, mfa_code=totp)

# my_stocks = holdings.stocks
# my_stocks = r.build_holdings()

PATH = "/home/hopper/chromedriver"

my_stocks = [
    "AMC",
    "AMD",
    "AMZN",
    "BABA",
    "BB",
    "BSIG",
    "CFII",
    "CVX",
    "DAL",
    "EPD",
    "ETSY",
    "FB",
    "GOOGL",
    "KO",
    "LAC",
    "MSFT",
    "NIO",
    "NTDOY",
    "NVDA",
    "POWW",
    "QQQ",
    "RCL",
    "RTX",
    "SNDL",
    "SPY",
    "SQ",
    "TEVA",
]
# Stopped at EPD

# holdingsFile = open("holdings.py", "a")
# holdingsFile.write(str(my_stocks))
# holdingsFile.close()

# soldFile = open("sold.py", "a")

# soldStocks = []








token_path = "token"

c = auth.client_from_token_file(token_path, config.api_key)

# positions = c.get_account(config.tda_acct_num, c.Account.Fields.POSITIONS)
# account_info = c.get_account(config.tda_acct_num, fields=[c.Account.Fields.POSITIONS]).json()
# print(account_info)

positions = c.Account.Fields.POSITIONS
r = c.get_account(config.tda_acct_num, fields=positions)

stocks = r.json()['securitiesAccount']['positions']

stocks = []

# for stock, data in my_stocks.items():
for stock in stocks:
    ticker = stock['instrument']['symbol']
    if ticker == 'MMDA1':
        continue
    driver = webdriver.Chrome(PATH)
    driver.get("https://financhill.com/search/stock-score/" + ticker)
    time.sleep(2)

    print(ticker)

    score = int(driver.find_element_by_tag_name("h2").text)
    print(score)

    if (score < 40):
        r.order_sell_trailing_stop(stock, data['quantity'], 1)
        soldStocks.append(stock)

    driver.quit()
# soldFile.write(soldStocks)
# soldFile.close()
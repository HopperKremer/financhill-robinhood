# For Robinhood, see hoptra
# Cancel all pending sell orders before running if you want to apply to every stock
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import config
import holdings

import robin_stocks as r
import pyotp

from selenium import webdriver
import time

# totp = pyotp.TOTP("My2factorAppHere").now()
# login = r.login(config.USERNAME, config.PASSWORD, mfa_code=totp)

# my_stocks = holdings.stocks
# my_stocks = r.build_holdings()

PATH = "/home/hopper/chromedriver"

my_stocks = ['AMC', 'AMD', 'AMZN', 'BABA', 'BB', 'BSIG', 'CFII', 'CVX', 'DAL', 'EPD', 'ETSY', 'FB', 'GOOGL', 'KO', 'LAC', 'MSFT', 'NIO', 'NTDOY', 'NVDA', 'POWW', 'QQQ', 'RCL', 'RTX', 'SNDL', 'SPY', 'SQ', 'TEVA']
# Stopped at EPD

# holdingsFile = open("holdings.py", "a")
# holdingsFile.write(str(my_stocks))
# holdingsFile.close()

soldFile = open("sold.py", "a")


soldStocks = []

# for stock, data in my_stocks.items():
for stock in my_stocks:
    driver = webdriver.Chrome(PATH)
    driver.get('https://financhill.com/search/stock-score/' + stock)
    time.sleep(2)

    print(stock)

    score = int(driver.find_element_by_tag_name('h2').text)
    print(score)

    # if (score < 40):
    #     r.order_sell_trailing_stop(stock, data['quantity'], 1)
    #     soldStocks.append(stock)

    driver.quit()
soldFile.write(soldStocks)
soldFile.close()
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
# login = r.login('hopperkremer@gmail.com', 'I<3linux24', mfa_code=totp)

my_stocks = holdings.stocks
# my_stocks = r.build_holdings()

PATH = "/home/hopper/chromedriver"

# stocks = ['AMC', 'AMD', 'AMZN', 'BABA', 'BB', 'BSIG', 'CFII', 'CVX', 'DAL', 'EPD', 'ETSY', 'FB', 'GOOGL', 'KO', 'LAC', 'MSFT', 'NIO', 'NTDOY', 'NVDA', 'POWW', 'QQQ', 'RCL', 'RTX', 'SNDL', 'SPY', 'SQ', 'TEVA']
# Stopped at EPD
for stock, data in my_stocks.items():
# for stock in stocks:
    # if i == 0:
    #     break

    driver = webdriver.Chrome(PATH)
    driver.get('https://financhill.com/search/stock-score/' + stock)
    time.sleep(2)

    print(stock)

    h2 = driver.find_element_by_tag_name('h2')
    print(h2.text)
    driver.quit()



print(holdings.stocks)

print(config.USERNAME)

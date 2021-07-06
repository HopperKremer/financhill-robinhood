# For Robinhood, see hoptrader.py for TD Ameritrade
# Cancel all pending sell orders before running if you want to apply to every stock
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import config

from selenium import webdriver
import time


PATH = "/home/hopper/chromedriver"

soldStocks = []

# for stock, data in my_stocks.items():
for stock in my_stocks:
    driver = webdriver.Chrome(PATH)
    driver.get("https://financhill.com/search/stock-score/" + stock)
    time.sleep(2)

    print(stock)

    score = int(driver.find_element_by_tag_name("h2").text)
    print(score)

    # if (score < 40):
    #     r.order_sell_trailing_stop(stock, data['quantity'], 1)
    #     soldStocks.append(stock)

    driver.quit()
soldFile.write(soldStocks)
soldFile.close()
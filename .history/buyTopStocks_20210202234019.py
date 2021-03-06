# from excel import OpenExcel
from tda import auth, client
import os, sys
import time

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
    c = auth.client_from_login_flow(
        driver, config.api_key, redirect_uri, config.token_path
    )

driver.get("https://financhill.com/screen/stock-score")
time.sleep(2)

button = driver.find_element_by_css_selector(
    'span[data-sort-name="stock_score_normalized"]'
)
time.sleep(2)

button.click()

tickers = driver.find_elements_by_tag_name("td")
for ticker in tickers:
    print(ticker.text)
    # print(ticker.tag_name)
    # print(ticker.parent)
    # print(ticker.location)
    # print(ticker.size)
# time.sleep(2)

driver.quit()

# for element in elements:
#     print(element.text())
# <span class="sort sort-desc" data-sort-name="stock_score_normalized" data-current-order="">Stock Score<i class="glyphicon"></i></span>
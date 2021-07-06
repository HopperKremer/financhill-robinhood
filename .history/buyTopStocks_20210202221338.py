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

# r = c.get_price_history(
#     "AAPL",
#     period_type=client.Client.PriceHistory.PeriodType.YEAR,
#     period=client.Client.PriceHistory.Period.TWENTY_YEARS,
#     frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
#     frequency=client.Client.PriceHistory.Frequency.DAILY,
# )
# assert r.status_code == 200, r.raise_for_status()
# print(json.dumps(r.json(), indent=4))

    driver = webdriver.Chrome(PATH)
    driver.get('https://financhill.com/screen/stock-score')

    score = int(driver.find_element_by_tag_name('h2').text)
    
    time.sleep(2)

    print(stock)
    print(score)

    driver.quit()
soldFile.write(soldStocks)
soldFile.close()


<span class="sort sort-desc" data-sort-name="stock_score_normalized" data-current-order="">Stock Score<i class="glyphicon"></i></span>
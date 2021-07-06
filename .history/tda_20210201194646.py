# from excel import OpenExcel
# tda.auth.client_from_manual_flow("HSBR8LJE3GSQA900VSZAX5GLJLLMO7K5", 'https://localhost:3000', 'https://api.tdameritrade.com/v1/oauth2/token', asyncio=False, token_write_func=None)
from tda import auth, client
import json
# Consumer Key	HSBR8LJE3GSQA900VSZAX5GLJLLMO7K5



# redirect_uri = 'https://your.redirecturi.com'
redirect_uri = 'https://localhost'
try:
    c = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome() as driver:
        c = auth.client_from_login_flow(
            driver, api_key, redirect_uri, token_path)

r = c.get_price_history('AAPL',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
assert r.status_code == 200, r.raise_for_status()
print(json.dumps(r.json(), indent=4))
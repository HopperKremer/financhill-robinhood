# Order to buy "quantity" shares of stock "ticker", with a 3% TSO and set a 10% TSO as soon as the order clears
def trailTrailBuy (ticker, quantity):
    order_template = {
    "orderStrategyType": "TRIGGER",
    "orderType": "TRAILING_STOP",
    "stopPriceOffset": 3, 
    "stopPriceLinkType": "PERCENT",
    "stopPriceLinkBasis": "BID",
    "stopType": "STANDARD",
    "session": "NORMAL",
    "duration": "GOOD_TILL_CANCEL",
    "orderStrategyType": "SINGLE",
    "orderLegCollection": [
        {
            "instruction": "BUY",
            "quantity": quantity,
            "instrument": {
                "symbol": ticker,
                "assetType": "EQUITY"
            }
        }
    ],
    #These are the child orders, these will take effect when the buy order is filled.
    "childOrderStrategies": [
    {
    "orderType": "TRAILING_STOP",
    "stopPriceOffset": 10, 
    "stopPriceLinkType": "PERCENT",
    "stopPriceLinkBasis": "BID",
    "stopType": "STANDARD",
    "session": "NORMAL",
    "duration": "GOOD_TILL_CANCEL",
    "orderStrategyType": "SINGLE",
    "orderLegCollection": [
        {
            "instruction": "SELL",
            "quantity": quantity,
            "instrument": {
                "symbol": ticker,
                "assetType": "EQUITY"
            }
        }
    ]
    }
    ]
    }
    return order_template

def setTrailingSell (ticker, quantity, trail):
    order_template = {
    "orderType": "TRAILING_STOP",
    "stopPriceOffset": trail, 
    "stopPriceLinkType": "PERCENT",
    "stopPriceLinkBasis": "BID",
    "stopType": "STANDARD",
    "session": "NORMAL",
    "duration": "GOOD_TILL_CANCEL",
    "orderStrategyType": "SINGLE",
    "orderLegCollection": [
        {
            "instruction": "SELL",
            "quantity": quantity,
            "instrument": {
                "symbol": ticker,
                "assetType": "EQUITY"
            }
        }
    ]
    }
    return order_template


tso = {
   "session":"NORMAL",
   "duration":"GOOD_TILL_CANCEL",
   "orderType":"TRAILING_STOP",
#    "cancelTime":"2021-06-09",
   "complexOrderStrategyType":"NONE",
   "quantity":1.0,
   "requestedDestination":"AUTO",
   "destinationLinkName":"AutoRoute",
   "stopPriceLinkBasis":"MARK",
   "stopPriceLinkType":"PERCENT",
   "stopPriceOffset":2.0,
   "stopType":"MARK",
   "orderLegCollection":[
      {
         "orderLegType":"EQUITY",
         "legId":1,
         "instrument":{
            "assetType":"EQUITY",
            "symbol":"MRNS"
         },
         "instruction":"SELL",
         "positionEffect":"CLOSING",
         "quantity":1.0
      }
   ],
   "orderStrategyType":"SINGLE",
   "cancelable":true,
#    "editable":false,
#    "status":"WORKING",
#    "accountId":233438563
}
print(tso)
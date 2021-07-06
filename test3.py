from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

import requests
from tda import auth, client
from tda.orders.equities import equity_buy_market, equity_buy_limit
from tda.orders.common import Duration, Session
import os, sys
import time
from selenium import webdriver
import json

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)
import config  # stored in parent directory for security


token_path = "token"

c = auth.client_from_token_file(token_path, config.api_key)


app = Flask(__name__)

print(1)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    print(2)
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    # if body == 'hello':
    #     resp.message("Hi!")
    # elif body == 'bye':
    #     resp.message("Goodbye")

    args = body.split(',')
    ticker = str(args[0])
    num_shares = args[1]

    print(3)

    order = equity_buy_market(ticker, int(num_shares))
    c.place_order(config.tda_acct_num, order)
    resp.message("Bought " + num_shares + " shares of " + body)
    print("Bought " + num_shares + " shares of " + body)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)
import config
print(config.tda_acct_num)
print(config.twilio_token)
# from inspect import getmembers, isfunction
# print(getmembers(config, isfunction))
# # /usr/bin/env python
# # Download the twilio-python library from twilio.com/docs/libraries/python
# import os
# from twilio.rest import Client

# # Find these values at https://twilio.com/user/account
# # To set up environmental variables, see http://twil.io/secure
# account_sid = config.twilio_id
# auth_token = config.twilio_token

# client = Client(account_sid, auth_token)

# client.api.account.messages.create(
#     to="+12316851234",
#     from_="+15555555555",
#     body="Hello there!")




from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6055529ec928297caf91165d51c30bbf"
# Your Auth Token from twilio.com/console
auth_token = config.twilio_token
# defd86f529261b018c0311dcbbc88ea5
client = Client(account_sid, auth_token)
client = Client("AC6055529ec928297caf91165d51c30bbf", "defd86f529261b018c0311dcbbc88ea5")

message = client.messages.create(
    to="+15183795333", 
    from_="+14194955394",
    body="Hello from Python!")

print(message.sid)
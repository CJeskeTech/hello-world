import os
from twilio.rest import Client

account_sid = 'AC4ec0fb6886fecd1155a3905fe59bda40'
auth_token = '8ee83bb272baeeb0e110bb66db9811c2'
client = Client(account_sid, auth_token)

message = client.messages.create(
		from_='+19034963536',
		body='hi mom it is me cameron',
		to='+15135328373',
)

print(message.sid)
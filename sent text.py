import os
from twilio.rest import Client

account_sid = 'account sid'
auth_token = 'auth token'
client = Client(account_sid, auth_token)

message = client.messages.create(
		from_='twilio #',
		body='message message message',
		to='phone number',
)

print(message.sid)
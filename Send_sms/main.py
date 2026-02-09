from twilio.rest import Client
import os

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)
message = client.messages.create(
  from_='+12232261415',
  body='Hello This is my first python project',
  to='+917989784200'
)
print(message.sid)
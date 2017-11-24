from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "1234"
# Your Auth Token from twilio.com/console
auth_token  = "1234"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+100000000",
    from_="+100000000",
    body="Hello!")

print(message.sid)

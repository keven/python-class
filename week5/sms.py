from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3f6a9b6f543683e0e2df5d4fe9b7783a"
# Your Auth Token from twilio.com/console
auth_token  = "aafe45ce8ba50903af654007273e0da6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16041111111",
    from_="+16043591132",
    body="Hello!")

print(message.sid)

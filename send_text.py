from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa3e9ae32fa703dc039771ec8aa75379a"
# Your Auth Token from twilio.com/console
auth_token  = "004e68e8816cf3313ecfd57e7c1a9ce4"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16039430184", #replace with your phone number
    from_="+16036051928", #replace with your twilio number
    body="My name is Clint Johnson!")

print(message.sid)

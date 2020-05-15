# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC654fb2b954a9b797a063c5210d5a4c50'
auth_token = '35c6be1371c069a40af2234fdd5c6859'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        from_="+12058392293",
        body="Join Earth's mightiest heroes. Like Capt. America .",
        # messaging_service_sid='MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        to='+918080103408'
    )

print(message.sid)

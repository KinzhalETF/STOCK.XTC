from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Replace with your Twilio phone number and recipient's phone number
from_number = 'YOUR_TWILIO_PHONE_NUMBER'
to_number = 'RECIPIENT_PHONE_NUMBER'

# Send an SMS
message = client.messages.create(
    body='Hello, this is a VoIP text message from Twilio!',
    from_=from_number,
    to=to_number
)

print(f"Message sent with SID: {message.sid}")

from twilio.rest import Client

sms_code = 'Q54DWRVPLCH4ZWYKJ1M9VT5M'


def send_message(sent_to, message):
    number = ""
    if sent_to[0] == "0":
        number = sent_to.replace("0", "", 1)
        number = '+66' + number
    account_sid = 'AC514cc1e3748f8e86e18c56d7c7c4691b'
    auth_token = 'fdbe724015389b3da236e76362e0115a'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+14243651467',
        body=message,
        to=number
    )

    print(f"sent SMS to {sent_to} successfully. ")

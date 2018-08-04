from smsapi import SmsApi

apikey = "675031xxxxxxxxxxxx"
sender = "SEDEMO"

sms = SmsApi(apikey, sender)

# Send SMS message to 902000xxxx - fill sender field "SENDER" and message with "MESSAGE"
sms = sms.send_sms(
    recipient="902000xxxx",
    message="test message"
)

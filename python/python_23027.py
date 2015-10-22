# Can't get status of sms from Twilio
body  = client.messages.get(sid)
status = body.status

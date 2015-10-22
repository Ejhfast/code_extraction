# Windows Azure Service Management from Python has certificate issue
openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem -subj "/CN=This Name Shows in the Portal"
openssl x509 -inform pem -in mycert.pem -outform der -out mycert.cer

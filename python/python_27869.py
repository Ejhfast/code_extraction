# How to get Python Requests to Trust a Self Signed SSL Certificate?
r = requests.post(url, data=data, verify='/path/to/public_key.pem')

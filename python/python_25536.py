# Clicking a Javascript link to make a post request in Python
payload = {'sem_ad_group__destination_url': 'yourTextValueHere'}
r = requests.post("theActionUrlForTheFormHere", data=payload)

# python do not follow redirect
headers = {"Accept-Language": "en-US,en;q=0.5"}
r = requests.get("https://mobile.bet365.com/sport/default.aspx", headers=headers)
print r.text

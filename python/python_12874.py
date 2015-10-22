# 403 error while getting data from Imgur api. Where am I going wrong?
headers = {"Content-Type": "text", "Authorization": "Client-ID YOUR_CLIENT_ID"}
r = requests.get("https://...", headers=headers, verify=False)

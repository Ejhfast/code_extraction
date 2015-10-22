# Find word in HTML page fast algorithm
def checkForWord():
    r = requests.get("http://example.com/somepage.html")
    return "myWord" in r.text

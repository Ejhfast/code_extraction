# does BeautifulSoup strips inline CSS and javascript content
''.join(BeautifulSoup(content).findAll(text=lambda text:
text.parent.name != "script" and
text.parent.name != "style"))

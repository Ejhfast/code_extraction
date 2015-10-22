# Regular expression to search only websites names from random text
import re
websites = re.findall(r'(\S+[.]com)', text)
# ['maangobar22.com', 'myapplesite22.com', 'berrymine22.com']

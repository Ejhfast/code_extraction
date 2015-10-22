# Python web scrapping involving HTML a tag
import re
names = soup.find_all("a",{"href":re.compile("dog")})

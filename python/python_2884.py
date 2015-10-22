# How to remove all html tags from downloaded page
import re
notag = re.sub("&lt;.*?&gt;", " ", html)

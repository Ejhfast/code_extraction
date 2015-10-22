# how to replace multiple characters in a string?
import re
newName = re.sub('[\\\\/:*?"&lt;&gt;|]', 'special char', name)

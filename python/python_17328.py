# Trying to remove tags but quickly running out of memory
import re
re.sub(r'&lt;[^&gt;]+&gt;', '', row)

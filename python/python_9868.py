# Generating Xml using python
import re
re.sub(r'number="([0-9]+)"',r"number='\1'", etree.tostring(root, pretty_print=True))

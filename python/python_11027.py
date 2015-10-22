# How to use Beautiful Soup to find a tag with changing id?
import re
for tag in soup.find_all(re.compile("^value_xxx_c_1_f_8_a_")):
    print(tag.name)

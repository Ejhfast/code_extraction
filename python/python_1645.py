# Parsing a range of integers in a list
for o in re.finditer('left:102[0-9]"&gt;&lt;nobr&gt;(.*?)&lt;/nobr&gt;&lt;/div&gt;', words[index]):
    out = o.group(1)

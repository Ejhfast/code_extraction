# How do I grab a number sandwiched between commas?
&gt;&gt;&gt; [item for item in line.split(',')[1:] if item.isdigit()][0]
'2503281'

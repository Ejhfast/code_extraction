# Regular expression to extract URLs with difficult formatting
m = re.findall("((http:|https:)//[^ \&lt;]*[^ \&lt;\.])",line)

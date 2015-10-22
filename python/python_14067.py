# Regex Python: Get Page and Subpage from URL
my_str = "/projects/myproject/"
matches = re.findall("/(.+?)/(.+)/",my_str)
print matches  #prints ['projects','myproject']

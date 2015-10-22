# Convert SRE_Match object to string
result = re.search(your_stuff_here)
if result:
    print result.group(0)

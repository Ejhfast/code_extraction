# Only print lines that are unique in the second column
if lowercaseusername not in lines_seen:
    lines_seen.add(lowercaseusername) # &lt;-- facepalm here
    print line.strip()

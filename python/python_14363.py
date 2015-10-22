# Searching for one of two complexish regex patterns in Python without creating submatches
re.findall("((?&lt;=^\[)[^[\]]+(?=\]$)|^[INTEXT]{3}\. .+?$)", text)

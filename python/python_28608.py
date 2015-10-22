# Delete a repeated character from only one specific position and not from all places of the string in python
s = 'bacdefaxyza'
idx = 6
s[:idx]+s[idx+1:]

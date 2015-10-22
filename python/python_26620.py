# Format a string with a space between every two digits
s = "534349511"
print ' '.join([s[i:i+2] for i in range(0,len(s),2)])

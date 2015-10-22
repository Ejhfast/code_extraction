# Searching of strings in a single string in python
for token in line.split(';'):
    start = any(s in token for s in ["RecentNetworks", "LastConnected"])

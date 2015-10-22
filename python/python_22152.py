# Joining elements in a list to a new list in Python
blocks = ["".join(adpcm_packets[i:i+13]) for i in range(0, len(adpcm_packets), 13)]

# Rename dictionary keys according to another dictionary
old = {change.get(k,k):v for k,v in old.items()}

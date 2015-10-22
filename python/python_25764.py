# str argument only functioning when submitted via single quotes as opposed to assigned variable
with open('shafile.txt', 'r') as f:
    value = f.read().strip()

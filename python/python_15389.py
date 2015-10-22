# Regex to find N numbers after some token in python
blar = re.search("Blar=(-?\d+\.\d+)((?:,-?\d+\.\d+)+)", x)
blar.groups()

# Programmatically figuring out if translated names are equivalent
def normalize(name):
    name_parts = name.replace("-", " ").split()
    return " ".join(sorted(name_parts)).lower()

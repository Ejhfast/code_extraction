# Are there any other ways to iterate through the attributes of a custom class, excluding the in-built ones?
for key, value in Terrain.__dict__.items():
    if not key.startswith("__"):
        print(...)

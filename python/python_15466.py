# Efficient list culling
generator = (item for item in a if item &gt; 10)
for item in generator:
    ...

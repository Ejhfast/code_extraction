# structured query language for JSON (in Python)
filtered_collection = From(some_collection).where("item.property &gt; 10").select_many()

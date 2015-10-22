# Update and delete, with value typed, in MySQL using Python
cursor.execute("DELETE FROM test WHERE name=%s", (Value,));

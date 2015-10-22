# Writing huge Mongo result set to disk w/ Python in a resource friendly way
with open("/path/to/storage/file", "w") as f:
    for row in cursor:
        f.write(row['your_field'])

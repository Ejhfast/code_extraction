# Boto doubles all get request cycles by design
key = Key(bucket=bucket, name=my_key_id)
data = key.get_contents_as_string()

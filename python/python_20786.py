# Unix sort producing wrong output
cat data.txt | python mapper.py | LC_COLLATE=C sort

# Python Text Encoding
with open('foo.txt', 'rb') as f:
    contents = f.read().decode('utf-8-sig')   # -sig takes care of BOM if present

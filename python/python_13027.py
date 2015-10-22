# zipfile several passwords match
if ord(h[11]) != check_byte:
    raise RuntimeError("Bad password for file", name)

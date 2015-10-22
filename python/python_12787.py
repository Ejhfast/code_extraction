# Python CSV to JSON parser add quotes to output
elif k == "alternatenames":
        r[k] = [name.strip() for name in v.split(",")]

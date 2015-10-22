# Add a restriction to a regex expression
vendor_id_stem = re.sub(r'(_[A-Za-z]*|_?[A-Za-z]{2,4}?\d?)$', "", vendor_id)

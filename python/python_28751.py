# Extract phone numbers with hyphen using Python regex
phone = re.search(r'(\d+-?){1,2}$', addr_str)

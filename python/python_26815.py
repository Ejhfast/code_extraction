# String manipulations using Python Pandas
frame3["name_len"] = frame3["name"].map(lambda x : len(re.findall('[a-zA-Z]', x)))

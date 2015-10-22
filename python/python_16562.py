# parsing repeated lines of string based on initial characters
all_data = " ".join([line for line in file]).split("ID")
return [", ".join([item.split(" ")[::2] for item in all_data])]

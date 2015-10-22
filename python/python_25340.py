# Remove double space/tab combinations using Re in Python
formatted_string = re.sub("[\t ]{2,}", " ", formatted_string)

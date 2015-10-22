# Does python have a better way to split a string than converting to a list?
rand = random.randint(6, len(split_name) - 1)
search_name = name[rand:] + '*'
rqst = requests.get(name_srch % (key, search_name))

# Filtering a list of lists of a tuple with regex
result_list = filter(lambda x: x, [[tup for tup in sub_list if re.match('1.3.6.1.2.1.4.24.7.1.7.1.4.172.16.0.100.32', str(tup[0]))] for sub_list in start_list])

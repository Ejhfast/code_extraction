# Loading .txt file as a dict, but exclude commented rows
list_of_dicts = [{key: value for (key, value) in zip(header, line.strip().split('; '))} for line in open('abcd.txt') if not line.strip().startswith('#')]

# python - list of dictionaries check key:value
name_pairs = set((i['name'], i['last']) for i in lst)
if (d['name'], d['last']) not in name_pairs:
    lst.append(d)

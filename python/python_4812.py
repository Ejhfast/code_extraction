# Match set of dictionaries. Most elegant solution. Python
def match_dict(new_list, old_list):
    old = dict((v['id'], v) for v in old_list)
    return [dict(d, **old[d['id']]) for d in new_list if d['id'] in old]

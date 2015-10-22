# Python - Dumping a dictionary to certain format
with open('some_namespace.belns', 'w') as fp:
    for key in sorted(hgnc_ns_dict):
        fp.write('    {0}|{1}\n'.format(key, hgnc_ns_dict[key]))

# Delete a dictionary from another dictionary python
dict((k, v) for (k, v) in parent_dict.iteritems() if k not in derived_dict)

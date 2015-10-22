# Prepairing list from a django query
list_col_b, list_col_c = zip(*MyModel.objects.values_list('col_b', 'col_c'))

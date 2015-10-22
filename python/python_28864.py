# Iter through defaultdict of defaultdict on Python 2.6
for url in apache_status_dict.keys():
  for req in apache_status_dict[url]:
      print apache_status_dict[url][req]

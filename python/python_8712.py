# What is Python's equivalent of "perl -V"
python -c 'import sysconfig, pprint; pprint.pprint(sysconfig.get_config_vars())'

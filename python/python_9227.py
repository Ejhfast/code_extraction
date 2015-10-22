# How do I output a config value in a Sphinx .rst file?
my_config_value = 42
rst_epilog = '.. |my_conf_val| replace:: %d' % my_config_value

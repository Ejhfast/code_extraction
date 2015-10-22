# Using dictionary comprehension with ConfigParser
def run_me(self):
    config_vars= self.get_properties('services','package_install','package_info')
    convig_vars_2 = self.get_properties('network','proxy_server','proxy_user')

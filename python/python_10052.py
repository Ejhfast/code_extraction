# Trac plugin development: How to get access to trac.ini item from plugin
def get(self, section, key, default=''):
     return self[section].get(key, default)

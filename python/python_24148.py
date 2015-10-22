# Permanently remove something from python sys.path
sys.path =  filter (lambda a: not a.startswith('/System'), sys.path)

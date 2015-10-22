# cx_freeze & pygobject in a subdirectory
os.environ['GI_TYPELIB_PATH'] = os.path.join(os.path.dirname(sys.executable),'bin\\lib\girepository-1.0')

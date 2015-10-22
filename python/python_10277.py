# How can I access the flask application configuration outside of the application?
cmd_folder = os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe() ))[0])
sys.path.append(cmd_folder+'/../')

# Set locale encoding in python
env = os.environ.copy()
env['LANG'] = 'en_US.UTF-8'
subprocess.check_output( ..., env = env)

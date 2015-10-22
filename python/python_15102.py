# virtualenv and subprocess.call() in mixed Python 2.7/3.3 environment
subprocess.call([sys.executable, 'yourscript.py'], env=os.environ.copy())

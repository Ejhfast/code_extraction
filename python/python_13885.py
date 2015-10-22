# Subprocess.call or Subprocess.Popen cannot use executables that are in PATH (Linux/Windows)
env = os.environ
proc = subprocess.Popen(args, env=env)

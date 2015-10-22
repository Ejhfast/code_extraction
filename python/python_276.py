# How do I run another script in Python without waiting for it to finish?
p = subprocess.Popen([sys.executable, '/path/to/script.py'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)

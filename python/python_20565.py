# Call one python script from inside the other script
subprocess.Popen(['python', 'script2', '-d', sys.argv[2]])

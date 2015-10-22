# Python: StringIO for Popen
p = subprocess.Popen(['grep', '...'], stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE)
output, output_err = p.communicate(myfile.read())

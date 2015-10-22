# Append file name to list comprehension
cfiles = [os.path.abspath(input_arg)+"/"+files for files in os.listdir(input_arg) if files.endswith(".c")]

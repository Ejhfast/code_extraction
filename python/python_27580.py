# execution error: The variable display is not defined. (-2753)
rest_command = """'display notification "{}" with title "{}"'""".format(meaning[0],word[0])
os.system("osascript -e "+ rest_command)

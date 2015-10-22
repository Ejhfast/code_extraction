# pass in popen parameters
constant_cmd_part = ["/path/to/program", "-opt", "-more_opt"]
proc = subprocess.Popen(constant_cmd_part + [variable_part],
                        stdout=subprocess.PIPE)

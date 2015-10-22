# Python: parse string as time given two possible formats
fmt = time_fmt_long if " " in input_string else time_fmt_short
dt = datetime.strptime(input_string, fmt)

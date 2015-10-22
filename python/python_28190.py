# regular expression: match everything but single forward- and double backslashes
re.match(r'(?!.*/|.*\\\\)', string)

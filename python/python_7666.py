# json.loads(jsonstring) in Python fails if string has a "\r" i.e. carriage return character
j="""{"data":"foo \\r\\n bar"}"""

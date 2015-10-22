# Is there a significant difference in assigning values one-by-one and with tuples in Python?
script_name, option1, option2, *_ = sys.argv # or
script_name, option1, option2 = sys.argv[:3]

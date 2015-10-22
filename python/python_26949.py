# How to match a regex in python, either completely or partially
regex_example = re.compile(
   '(\d{10}\s\d-\d(?:\d{0,2}(?:(?:-\d{0,3})?(?:-\d{0,4})?)?)?)')

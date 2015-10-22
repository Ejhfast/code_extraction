# How to sort list of String without considering Special characters and with case insensitive
sorted(list1, key=lambda x: re.sub('[^A-Za-z]+', '', x).lower())

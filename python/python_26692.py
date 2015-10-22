# TypeError: 'str' does not support the buffer interface issue
reader = csv.DictReader(open("Test.csv", "r", newline=''))
writer = csv.DictWriter(open("Test1.csv", "w", newline=''), fieldnames=writenames)

# How to sort in python with multiple conditions?
finalresult = sorted(result, key=lambda word: (-word[1], len(word[0]), word[0]))

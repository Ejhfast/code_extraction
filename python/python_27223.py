# Loop through list based on number of characters of user input
for count, letter in enumerate(newMessage):
    foundAt = myList[count % len(myList)].find(letter)

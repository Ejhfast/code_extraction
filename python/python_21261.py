# I'm trying to get python to print a random word from the list but instead it just prints the whole list. Can someone suggest any ways to fix this?
friends_count = 2
friends = [input("Type in your friend's name:") for _ in range(friends_count)]
print(random.choice(friends))

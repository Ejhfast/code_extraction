# Correct syntax to remove list elements by value from MySQL array
existingEpisodeIDs = [row[0] for row in c.fetchall()] #this will end up just being a list of id's
id = 22528819
existingEpisodeIDs.remove(id)

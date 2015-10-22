# facepy: How do I get a list, by friend, of pages liked by my friends using facepy?
friend_likes = graph.get('me?fields=friends.fields(likes)')
friend_likes['friends']

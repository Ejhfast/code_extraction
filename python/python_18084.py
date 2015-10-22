# facebook get friends' birthdays using python
args = {'fields' : 'birthday,name' }
friends = graph.get_object("me/friends",**args)

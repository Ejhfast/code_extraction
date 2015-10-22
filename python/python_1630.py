# How do I get the "Interests" of a facebook user uing Facebook Connect? (I'm using Django/python and pyFacebook middleware)
fbdata = request.facebook.users.getInfo(request.facebook.uid,
                                        ['name', 'pic', 'interests'])

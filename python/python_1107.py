# Copying values from a dictionary into an object in Python
for key, value in post.iteritems():
    setattr(my_model, key, value)

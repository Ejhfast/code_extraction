# How to get number of objects in a pickle?
pickle.dump(len(objects), fileobj)
for ob in objects:
    pickle.dump(ob, fileobj)

# How to for-loop output in python?
actors = [item.text for item in soup.findAll('span', {"itemprop":"actor"})]
print "Actors: %s" % (", ".join(actors))

# What is right way to build database with deep dependencies in Django?
SomeDeeperStuff.objects.filter(somestuff__worker__company__user=user)

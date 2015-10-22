# Selecting related objects in django
claimer = User.objects.get(name='test')
claimed_opponents = User.objects.filter(gameclaim_opponent__me__user=claimer)

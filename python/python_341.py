# Django, Python Loop Logic Problem
def get_jobrecord_cost(self):
    return sum((activity.get_cost() or 0 for activity in activity_set.all()) or 0)

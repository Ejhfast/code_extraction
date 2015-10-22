# Django Templatetag, List index out of range
def random_fact():
    fact = Fact.objects.order_by('?').first()
    return {'fact': fact}

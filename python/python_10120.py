# Celery PeriodicTask arguments
def run(self, **kwargs):
    value = get_value_from_database()
    print 'Passed value %s' % value

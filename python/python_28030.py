# Filter latest record in Django
def get_latest_report():
    """ Returns the latest report from each app """
    return [app.report_set.latest('date') for app in App.objects.all()]

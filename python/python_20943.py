# Dictionary to table in django
def panel(request):
    adlist = [{'title': 'haas', 'price': 12.50, 'bid': 50.0, 'seen': 23.11}]
    return render(request, 'panel.html', {'adlist' : adlist})

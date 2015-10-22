# django getting variable from url into view
def next_page(request,location_id):
    loc = Location.objects.get(id=location_id)

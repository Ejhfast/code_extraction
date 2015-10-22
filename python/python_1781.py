# geodjango - search by city, state or zip code
zip = 10010
zipcode = ZipCode.objects.get(number=zip)
Store.objects.filter(coordinates__in=zipcode)

# QuerySet to get all attributes for a user's contacts?
p = UserProfile.objects.get(id=1)
contacts = p.mutual_contacts()
positions = Position.objects.filter(positiontimestamp__profile__in=contacts)

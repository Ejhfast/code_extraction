# How can django sql queries use case insensitive and contains at the same time?
User.objects.filter(username__icontains='ab')

# Search M2M fields by names not by id in django
contadores = Profile.objects.filter(specialities__name__iexact = request.POST['buscar'])

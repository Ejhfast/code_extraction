# Filter a reverse manytomany django in one line?
administrators = User.objects.filter(leagueadministrator__league__id=1).distinct()

# currentTeams = StraightredTeam.objects.filter(currentteam=1).exclude(teamid__in=cantSelectTeams.values_list('teamselectionid', flat=True)).order_by('teamshortname')

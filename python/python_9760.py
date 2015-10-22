# Django Error Message: You can't set team_name (a non-nullable field) to None
class UserProfile(models.Model):
        user = models.OneToOneField(User)
        team_name = models.ForeignKey(Team_Profile, default=0)

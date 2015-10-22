# Can Django have a ManyToMany relationship with global_settings.LANGUAGES?
class LanguageSpoken(models.Model):
     user = models.ForeignKey("UserProfile")
     language = models.CharField(max_length = 2, choices = LANGUAGES)

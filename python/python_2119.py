# Django syncdb error: One or more models did not validate
class notes(models.Model):
    created_by = models.ForeignKey(User, related_name="note_created_by_user")
    detail = models.ForeignKey(Details, related_name="noted_and_detailed")

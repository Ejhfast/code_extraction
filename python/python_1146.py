# Django unique_together and flagging objects as "deleted"
class Meta:
     unique_together = ( ('name', 'active'),)

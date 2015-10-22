# How to extend django abstract base model by inheritance?
class RecordModel(TimeStampedModel):
    class Meta(TimestampedModel.Meta):
        abstract = True

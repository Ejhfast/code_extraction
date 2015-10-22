# Django MongoEngine/REST Framework ListFields
enabled = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=4096)
    )

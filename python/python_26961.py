# Django rest serializer.data is an empty OrderedDict()
class StaffSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  content = serializers.CharField(max_length=200)

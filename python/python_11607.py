# Reverse Relationship with Tastypie, AttributeError
def dehydrate(self, bundle):
        bundle.data['votes'] = Vote.objects.filter(object_id=bundle.obj.id, content_type=n).count() // or use aggregate to get total votes.
        return bundle.date

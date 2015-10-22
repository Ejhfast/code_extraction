# POST multiple objects in one TastyPie API request
class GameResource(ModelResource):
    activities = fields.ToManyField(ActivityResource, 'activities', full=True)

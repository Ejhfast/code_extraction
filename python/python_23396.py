# Django Tastypie Generic Relation
class WorkResource( BaseModelResource ):
    links = fields.ToManyField('musiclibrary.api.LinkResource', attribute=lambda bundle: Link.objects.filter(entity0_content_type=ContentType.objects.get_for_model(bundle.obj), entity0_object_id=bundle.obj.id))

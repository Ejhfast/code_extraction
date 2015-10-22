# Custom related name for a Django model parent link?
class MySubclass(MyBaseClass):
    mybaseclass = models.OneToOneField(MyBaseClass, parent_link=True, related_name='thissubclass')

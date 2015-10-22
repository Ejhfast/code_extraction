# Getting a Caught NoReverseMatch error in django
urlpatterns = patterns('tiptop.views',
    (r'^(\d+)/(\d*)$', 'test_items'),
)

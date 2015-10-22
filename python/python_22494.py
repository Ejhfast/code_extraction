# django rest framework: routers.DefaultRouter() url with custom path
urlpatterns = patterns('',
url(r'^api/', include(router.urls)),
url(r'^test/add/$',  TestNewViewSet.as_view(), name='whatever'),

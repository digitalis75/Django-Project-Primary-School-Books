from django.conf.urls import url
from .views import do_search, search_by_class

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^(?P<stage>[\w\-]+)/$', search_by_class, name='search_by_class')
]

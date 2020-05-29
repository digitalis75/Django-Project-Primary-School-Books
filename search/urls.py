from django.conf.urls import url
from .views import do_search, search_by_class, search_by_class_subject

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^(?P<stage>[\w\-]+)/$', search_by_class, name='search_by_class'),
    url(r'^(?P<stage>[\w\-]+)/(?P<subject>[\w\-]+)/$', search_by_class_subject,
        name='search_by_class_subject')
]

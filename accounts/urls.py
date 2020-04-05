from django.conf.urls import url
from .views import login, logout, registration

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', registration, name='registration'),
]

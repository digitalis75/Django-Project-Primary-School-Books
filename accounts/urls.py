from django.conf.urls import url, include
from .views import login, logout, registration
from . import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', registration, name='registration'),
    url(r'^password_reset/', include(url_reset))
]

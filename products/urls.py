from django.conf.urls import url
from .views import all_products, product_info

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<slug>[\w-]+)/$', product_info, name='product_info'),
]

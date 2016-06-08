from django.conf.urls import url
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    url(
        r'^products$',
        ProductListCreateView.as_view(),
        name='product-list-create'
    ),
    url(
        r'^products/(?P<product_id>[0-9]+)$',
        ProductRetrieveUpdateDestroyView.as_view(),
        name='product-detail'
    ),
]

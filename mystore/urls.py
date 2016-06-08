
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('applications.products.urls')),
    url(r'^api/', include('rest_framework_swagger.urls')),
]

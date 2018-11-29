
from django.contrib import admin
# # from django.urls import path
# from django.url.conf import include, url
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/', include('rest_auth.urls')),
    url(r'^api/registration/', include('rest_auth.registration.urls')),
]

from django.conf.urls import url, include
from django.contrib import admin

from childcare_app.views import IndexView, UserCreateView, ChildCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^create_child/$', ChildCreateView.as_view(), name="child_create_view"),
]

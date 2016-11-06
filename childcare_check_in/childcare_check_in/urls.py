from django.conf.urls import url, include
from django.contrib import admin

from childcare_app.views import IndexView, UserCreateView, ChildCreateView, CheckCreateView, \
                                CheckUpdateView, ProfileListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^accounts/profile/$', ProfileListView.as_view(), name="profile_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^create_child/$', ChildCreateView.as_view(), name="child_create_view"),
    url(r'^check_in/(?P<pk>\d+)/$', CheckCreateView.as_view(), name="check_create_view"),
    url(r'^check_out/(?P<pk>\d+)/$', CheckUpdateView.as_view(), name="check_update_view"),
    # url(r'^child_check_in/(?P<pk>\d+)/$', ChildCreateView.as_view(), name="child_create_view"),
    # url(r'^child_check_out/(?P<pk>\d+)/$', ChildUpdateView.as_view(), name="child_update_view"),
    ]

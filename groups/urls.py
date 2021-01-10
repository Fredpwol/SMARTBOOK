from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

app_name = 'groups'
urlpatterns = [
    url(r'^$',views.ListGroups.as_view(),name='all'),
    url(r'^create/$',views.CreateGroup.as_view(),name='create'),
    url(r'^posts/in(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='single'),
    url(r'^join/(?P<slug>[-\w]+)/$',views.JoinGroup.as_view(),name='join'),
    url(r'^leave/(?P<slug>[-\w]+)/$',views.LeaveGroup.as_view(),name='leave')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
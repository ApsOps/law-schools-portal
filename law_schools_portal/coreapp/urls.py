from django.conf.urls import patterns, include, url
from .views import HomePageView, SignUpView, LoginView, LogOutView, WorkView

urlpatterns = patterns('',

    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),
    url(r'^work/$', WorkView.as_view(), name='work'),

)

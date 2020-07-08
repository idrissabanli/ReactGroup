from django.urls import path, re_path
from accounts.views import register, activate, login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    # path('logout/', logout, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
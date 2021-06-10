from django.urls import path

from app_login.views import *

urlpatterns = [
    path('signup', signup, name='signup', ),
    path('login', login_user, name='login', ),
    path('logout', logout_user, name='logout', ),
    path('profile-change', user_profile_change,  name='user_profile_change', )


]
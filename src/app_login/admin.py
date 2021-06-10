from django.contrib import admin

from app_login.models import *


admin.site.register(CustomUser)
admin.site.register(Profile)


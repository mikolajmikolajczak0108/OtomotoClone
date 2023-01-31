from django.contrib import admin
from .models import MyUser
from .models import Profile


admin.site.register(MyUser)
admin.site.register(Profile)

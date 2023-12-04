from django.contrib import admin
from accounts.models.users import User
from accounts.models.profiles import Profile
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
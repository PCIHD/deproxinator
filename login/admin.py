from django.contrib import admin
from login.models import UserProfileInfo,LoggedUser,AdminKey,AdminRegistrationModel
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(LoggedUser)
admin.site.register(AdminKey)
admin.site.register(AdminRegistrationModel)

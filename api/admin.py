from django.contrib import admin
from .models import UserModel,EstateModel, ImageModel

admin.site.register(UserModel)
admin.site.register(EstateModel)
admin.site.register(ImageModel)

from django.contrib import admin
from .models import Advertisement

# Register your models here.
class AdvertisementsAdmin(admin.ModelAdmin):
    ...

admin.site.register(Advertisement, AdvertisementsAdmin)
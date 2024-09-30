from django.contrib import admin
from PetTracker.models import Organization, Foster, Pet

# Register your models here.

admin.site.register(Pet)
admin.site.register(Organization)
admin.site.register(Foster)
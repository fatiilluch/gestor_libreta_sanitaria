from django.contrib import admin
from .models import Pet, Vacune, Antiparasitic

# Register your models here.
admin.site.register(Pet)
admin.site.register(Vacune)
admin.site.register(Antiparasitic)

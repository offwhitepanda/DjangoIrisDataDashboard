from django.contrib import admin
from .models import Observation,Species

# Register your models here.
admin.site.register(Observation)
admin.site.register(Species)
from django.contrib import admin
from .models import Bibelot


class BibelotAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)



admin.site.register(Bibelot, BibelotAdmin)
 

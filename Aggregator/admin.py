from django.contrib import admin
from .models import *
# Register your models here.

class ProgContentAdmin(admin.ModelAdmin):
    list_display = ('headline', 'img', 'url')

class HiringContentAdmin(admin.ModelAdmin):
    list_display = ('headline', 'img', 'url')


class PyContentAdmin(admin.ModelAdmin):
    list_display = ('headline', 'img', 'url')


class CovidContentAdmin(admin.ModelAdmin):
    list_display = ('headline', 'img', 'url')

admin.site.register(ProgContent,ProgContentAdmin)
admin.site.register(HiringContent,HiringContentAdmin)
admin.site.register(PyContent,PyContentAdmin)
admin.site.register(CovidContent,CovidContentAdmin)

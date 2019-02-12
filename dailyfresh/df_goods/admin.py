from django.contrib import admin
from .models import TypeInfo, GoodsInfo


# Register your models here.
class TypeIndoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']


class GoodsIndoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'gtitle', 'gprice', 'gunit', 'gclick', 'gkucun', 'gcontent', 'gtype']


admin.site.register(TypeInfo, TypeIndoAdmin)
admin.site.register(GoodsInfo, GoodsIndoAdmin)


from django.contrib import admin
from sgroups.models import Sgroup, Leader

# Register your models here.

class LeaderAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'picture', 'gender']
    list_display = ('name', 'email', 'picture')

class SgroupAdmin(admin.ModelAdmin):
    fields = ['name', 'book', 'leader', 'leader2', 'coordinator', 'location','address',
    'day', 'time', 'group_type', 'description']
    list_display = ('name', 'book', 'leader', 'leader2', 'coordinator', 'location','address',
    'day', 'time', 'group_type', 'description')

admin.site.register(Leader, LeaderAdmin)
admin.site.register(Sgroup, SgroupAdmin)
from django.contrib import admin
from groups.models import Group, Leader

# Register your models here.

class LeaderAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'picture', 'gender']
    list_display = ('name', 'email', 'picture')

class GroupAdmin(admin.ModelAdmin):
    fields = ['name', 'group_style', 'book', 'leader', 'leader2', 'leader3', 'coordinator', 'picture', 'location','address',
    'day', 'time', 'group_type', 'description']
    list_display = ('name', 'group_style', 'book', 'leader', 'leader2', 'leader3', 'coordinator', 'picture', 'location','address',
    'day', 'time', 'group_type', 'description')

admin.site.register(Leader, LeaderAdmin)
admin.site.register(Group, GroupAdmin)

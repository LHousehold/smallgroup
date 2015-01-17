from django.contrib import admin
from groups.models import Group, Leader

# Register your models here.

class LeaderAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'picture', 'gender']
    list_display = ('name', 'email', 'picture')

class GroupAdmin(admin.ModelAdmin):
    fields = ['name', 'leader', 'picture', 'location', 'day', 'time', 'group_type']
    list_display = ('name', 'leader', 'picture', 'location', 'day', 'time', 'group_type')

admin.site.register(Leader, LeaderAdmin)
admin.site.register(Group, GroupAdmin)
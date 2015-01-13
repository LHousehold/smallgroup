from django.contrib import admin
from leaders.models import Leader

# Register your models here.

class LeaderAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'picture', 'gender']
    list_display = ('name', 'email', 'picture')

admin.site.register(Leader, LeaderAdmin)

from django.contrib import admin
from leaders.models import Leader

# Register your models here.

class LeaderAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'gender']
    list_display = ('name', 'email', 'gender')

admin.site.register(Leader, LeaderAdmin)

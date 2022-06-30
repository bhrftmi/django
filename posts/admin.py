from django.contrib import admin
from .models import post,comment
# Register your models here.

class commentAdminInline(admin.TabularInline):
    model = comment
    #fields = ['text','created_time']
    fields = ['text']
    extra = 0

#@admin.register(post) #decorator
class postAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'is_enabled' , 'publish_date','created_time','update_time']
    inlines = [commentAdminInline]

class commentAdmin(admin.ModelAdmin):
    list_display = ['text']




admin.site.register(post,postAdmin) #or before class definition @admin.register(post)
#admin.site.register(comment,commentAdmin)
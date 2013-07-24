from django.contrib import admin
from models import User, Post


class UserAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('email', 'is_active', 'is_staff', 'is_superuser', 'last_login')
        }),
        ('Groups & Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions')
        }),
    )
    list_display = ('email', 'is_staff', 'last_login')
    search_fields = ['email']
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'last_login')
    filter_horizontal = ['groups', 'user_permissions']


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'url', 'author', 'time_published', 'time_modified')
    search_fields = ['title', 'url', 'content']
    list_filter = ('time_published', 'time_modified')


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)

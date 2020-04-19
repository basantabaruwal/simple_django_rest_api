from django.contrib import admin
from .models import User, UserFeedItem


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_staff', 'is_superuser', )
    list_display_links = ('id', 'name', 'email',)
        
# admin.site.register(User, UserAdmin)


@admin.register(UserFeedItem)
class UserFeedItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status_text', 'created_on',)
    list_display_links = ('id', 'user', )


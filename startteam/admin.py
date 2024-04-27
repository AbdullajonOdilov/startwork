from django.contrib import admin
from .models import User, Projects, Orders, Team, Images

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'position', 'status')  # Fields displayed in the list view
    search_fields = ('username', 'full_name', 'position')           # Fields searchable in the admin interface
    list_filter = ('status',)                           # Filters displayed on the right sidebar
    fieldsets = (
        (None, {
            'fields': ('full_name', 'position', 'skills', 'image', 'address', 'status', 'contacts', 'education')
        }),
        ('Additional Information', {
            'fields': ('projects_number', 'balance'),
            'classes': ('collapse',)  # Hide this section by default
        }),
    )

# Register the User model with the custom admin class
admin.site.register(User, UserAdmin)
admin.site.register(Projects)
admin.site.register(Orders)
admin.site.register(Team)
admin.site.register(Images)

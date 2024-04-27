from django.contrib import admin
from .models import User, Projects, Orders, Team, Images
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# Register your models here.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'full_name', 'position', 'skills', 'image', 'address', 'status', 'contacts', 'education', 'projects_number', 'balance')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'full_name', 'position', 'status')  
    search_fields = ('username', 'full_name', 'position')           
    list_filter = ('status',)                           
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'full_name', 'position', 'skills', 'image', 'address', 'status', 'contacts', 'education')
        }),
        ('Additional Information', {
            'fields': ('projects_number', 'balance'),
            'classes': ('collapse',)  
        }),
    )

admin.site.register(User, CustomUserAdmin)

# Register the User model with the custom admin class
admin.site.register(Projects)
admin.site.register(Orders)
admin.site.register(Team)
admin.site.register(Images)

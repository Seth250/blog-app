from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserSignUpForm
from django.contrib.auth import get_user_model

# Register your models here.

class CustomUserAdmin(UserAdmin):
	add_form = UserSignUpForm
	# form = CustomUserChangeForm
	model = get_user_model()
	list_display = ('email', 'is_staff', 'is_active')
	list_filter = ('email', 'is_staff', 'is_active')
	fieldsets = (
		(None, {'fields': ('email', 'password')}), 
		('Permissions', {'fields': ('is_staff', 'is_active')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide', ), 
			'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
			}
		),
	)
	search_fields = ('email', )
	ordering = ('email', )

admin.site.register(get_user_model(), CustomUserAdmin)

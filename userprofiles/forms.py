from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from .models import Profile


class BaseModelForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		kwargs.setdefault('label_suffix', '')
		return super(BaseModelForm, self).__init__(*args, **kwargs)


class UserUpdateForm(UserChangeForm):
	password = None
	readonly_fields = ('email', )
			
	class Meta:
		model = get_user_model()
		fields = ('email', 'first_name', 'last_name', ) #'username', 'date_of_birth', 'profile_image' 'date_joined'
		widgets = {
			'email': forms.EmailInput(attrs={
				'class': 'read-only text-input-acc pfl-col__input-box'
			}),
			'first_name': forms.TextInput(attrs={
				'class': 'text-input-acc pfl-col__input-box'
			}),
			'last_name': forms.TextInput(attrs={
				'class': 'text-input-acc pfl-col__input-box'
			}),
			# 'date_joined': forms.DateInput(attrs={
			# 	'class': 'text-input-acc read-only pfl-col__input-box'
			# }),
		}

	def __init__(self, *args, **kwargs):
		kwargs.setdefault('label_suffix', '')
		super(UserUpdateForm, self).__init__(*args, **kwargs)
		for field in self.readonly_fields:
			self.fields[field].disabled = True


class ProfileUpdateForm(BaseModelForm):

	class Meta:
		model = Profile
		fields = ('date_of_birth', 'image')
		widgets = {
			'date_of_birth': forms.DateInput(attrs={
				'type': 'date',
				'class': 'text-input-acc pfl-col__input-box'
			})
		}

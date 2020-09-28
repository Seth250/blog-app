from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from blog.forms import BaseModelForm


class UserUpdateForm(UserChangeForm):
	password = None
	readonly_fields = ('email', )
			
	class Meta:
		model = get_user_model()
		fields = ('email', 'first_name', 'last_name', 'username')
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
			'username': forms.TextInput(attrs={
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

	def clean_username(self):
		cleaned_data = super(UserUpdateForm, self).clean()
		username = cleaned_data['username']
		if get_user_model().objects.filter(username__iexact=username).exists() and self.instance.username != username:
			self.add_error('username', 'This username has been already been taken')

		return username


class ProfileUpdateForm(BaseModelForm):

	class Meta:
		model = Profile
		fields = ('bio', 'date_of_birth', 'image')
		widgets = {
			'bio': forms.Textarea(attrs={
				'class': 'text-input-acc pfl-col__input-box'
			}),
			'date_of_birth': forms.DateInput(attrs={
				'type': 'date',
				'class': 'text-input-acc pfl-col__input-box'
			})
		}

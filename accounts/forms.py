from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from userprofiles.models import Profile
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from PIL import Image


class UserSignUpForm(UserCreationForm):

	password1 = forms.CharField(
        label=_("Password"),
        strip=False,
		widget=forms.PasswordInput(
			attrs={
				'auto-complete': 'new-password',
				'class': 'text-input-acc password-input'
			}
		)
	)

	password2 = forms.CharField(
	    label=_('Confirm Password'),
	    strip=False,
		widget=forms.PasswordInput(
			attrs={
				'auto-complete': 'new-password',
				'class': 'text-input-acc password-input'
			}
		)
	)

	class Meta:
		model = get_user_model()
		fields = ('email', 'first_name', 'last_name')
		widgets = {
			'email': forms.EmailInput(
				attrs={'class': 'text-input-acc standard-input'}
			),
			'first_name': forms.TextInput(
				attrs={'class': 'text-input-acc standard-input'}
			),
			'last_name': forms.TextInput(
				attrs={'class': 'text-input-acc standard-input'}
			)
		}

	def __init__(self, *args, **kwargs):
		kwargs.setdefault('label_suffix', '')
		return super(UserSignUpForm, self).__init__(*args, **kwargs)

	@transaction.atomic
	def save(self, commit=True):
		user = super().save(commit=False)

		if commit:
			user.save()
			profile = Profile.objects.create(user=user)

		return user


class CustomAuthenticationForm(AuthenticationForm):
	username = UsernameField(
		widget=forms.EmailInput(
			attrs={'class': 'text-input-acc standard-input'}
		)
	)

	password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
        	attrs={
        		'autocomplete': 'new-password',
        		'class': 'text-input-acc password-input'
        	}
        ),
	)

	def __init__(self, request=None, *args, **kwargs):
		kwargs.setdefault('label_suffix', '')
		super(CustomAuthenticationForm, self).__init__(request, *args, **kwargs)

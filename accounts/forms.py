from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


class UserSignUpForm(UserCreationForm):
	username = forms.CharField(
		max_length = 25,
		widget=forms.TextInput(
			attrs={}
		)
	)

	email = forms.EmailField(
		label=_('Email Address'), 
		required=True
	)

	password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
        	attrs={'autocomplete': 'new-password'}
        ),
	)

	password2 = forms.CharField(
	    label=_('Confirm Password'),
	    strip=False,
	    widget=forms.PasswordInput(
	    	attrs={'autocomplete': 'new-password'}
	    )
	)

	class Meta():
		model = get_user_model()
		fields = ('username', 'email', )

		# def clean_username(self):
		# 	cleaned_data = super().clean()
		# 	username = cleaned_data.get("username")
		# 	if username and self.model.objects.filter(username__iexact=username).exists():
		# 		self.add_error('username', 'This Username already exists')

		# 	return username 
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


class UserSignUpForm(UserCreationForm):
	username = forms.CharField(
		max_length = 25,
		widget=forms.TextInput(
			attrs={
				'class': 'text-input standard-input'
			}
		),
		label_suffix=""
	)

	email = forms.EmailField(
		label=_('Email Address'), 
		label_suffix="",
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'text-input standard-input'
			}
		),
	)

	password1 = forms.CharField(
        label=_("Password"),
        label_suffix="",
        strip=False,
        widget=forms.PasswordInput(
        	attrs={
        		'autocomplete': 'new-password',
        		'class': 'text-input password-input'
        	}
        ),
	)

	password2 = forms.CharField(
	    label=_('Confirm Password'),
	    label_suffix="",
	    strip=False,
	    widget=forms.PasswordInput(
	    	attrs={
	    		'autocomplete': 'new-password',
	    		'class': 'text-input password-input'
	    	}
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
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _
from PIL import Image


class UserSignUpForm(UserCreationForm):
	username = forms.CharField(
		max_length = 25,
		widget=forms.TextInput(
			attrs={
				'class': 'text-input-acc standard-input'
			}
		),
		label_suffix=""
	)

	email = forms.EmailField(
		label=_('Email Address'), 
		label_suffix="",
		required=True,
		widget=forms.EmailInput(
			attrs={
				'class': 'text-input-acc standard-input'
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
        		'class': 'text-input-acc password-input'
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
	    		'class': 'text-input-acc password-input'
	    	}
	    )
	)

	class Meta:
		model = get_user_model()
		fields = ('username', 'email', )

		def clean_username(self):
			cleaned_data = super(UserSignUpForm, self).clean()
			username = cleaned_data.get("username")
			if len(username) < 4:
				self.add_error('username', 'Username cannot be less than 4 characters')

			elif self.model.objects.filter(username__iexact=username).exists():
				self.add_error('username', 'This Username already exists')

			return username 


class CustomAuthenticationForm(AuthenticationForm):
	username = forms.CharField(
		max_length = 25,
		label_suffix="",
		widget=forms.TextInput(
			attrs={
				'class': 'text-input-acc standard-input'
			}
		)
	)

	password = forms.CharField(
        label_suffix="",
        strip=False,
        widget=forms.PasswordInput(
        	attrs={
        		'autocomplete': 'new-password',
        		'class': 'text-input-acc password-input'
        	}
        ),
	)


class UserUpdateForm(UserChangeForm):
	password = None
	readonly_fields = ('username', 'date_joined')

	def __init__(self, *args, **kwargs):
		super(UserUpdateForm, self).__init__(*args, **kwargs)
		for field in self.readonly_fields:
			self.fields[field].disabled = True
			
	class Meta:
		model = get_user_model()
		fields = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'date_of_birth', 'profile_image')
		widgets = {
			'username': forms.TextInput(attrs={
				'class': 'read-only text-input-acc pfl-col__input-box'
			}),
			'email': forms.EmailInput(attrs={
				'class': 'text-input-acc pfl-col__input-box'
			}),
			'first_name': forms.TextInput(attrs={
				'class': 'text-input-acc pfl-col__input-box'
			}),
			'last_name': forms.TextInput(attrs={
				'class': 'text-input-acc pfl-col__input-box'
			}),
			'date_joined': forms.DateInput(attrs={
				'class': 'text-input-acc read-only pfl-col__input-box'
			}),
			'date_of_birth': forms.DateInput(attrs={
				'type': 'date',
				'class': 'text-input-acc pfl-col__input-box'
			})
		}

	def clean_profile_image(self):
		cleaned_data = super(UserUpdateForm, self).clean()
		profile_image = cleaned_data['profile_image']
		if not profile_image:
			return profile_image

		img = Image.open(profile_image.file)
		if img.height > 150 or img.width > 150:
			output_size = (150, 150)
			extension = img.format.lower()
			img = img.resize(output_size, Image.LANCZOS)
			profile_image.file = type(profile_image.file)()
			img.save(profile_image.file, extension, optimize=True)

		return profile_image
		
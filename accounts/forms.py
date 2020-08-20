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

	class Meta:
		model = get_user_model()
		fields = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'date_of_birth', 'profile_image')
		widgets = {
			'username': forms.TextInput(attrs={
				'readonly': 'readonly',
				'class': 'read-only'
			}),
			'email': forms.TextInput(attrs={
				# 'readonly': 'readonly',
				'class': 'read-only'
			}),
			'date_joined': forms.DateInput(attrs={
				'readonly': 'readonly',
				'class': 'read-only'
			}),
			'last_login': forms.DateTimeInput(attrs={
				'readonly': 'readonly',
				'class': 'read-only'
			}),
			'date_of_birth': forms.DateInput(attrs={
				'type': 'date',
				'class': 'date-input'
			})

		}

	def clean_profile_image(self):
		cleaned_data = super(UserUpdateForm, self).clean()
		profile_image = cleaned_data['profile_image']
		if not profile_image:
			return profile_image

		img = Image.open(profile_image.file)
		if img.height > 250 or img.width > 250:
			output_size = (250, 250)
			extension = img.format.lower()
			img.thumbnail(output_size)
			# Resetting io.BytesIO object, otherwise resized image bytes will get appended to the original image
			profile_image.file = type(profile_image.file)()
			img.save(profile_image.file, extension)

		return profile_image

	# def save(self):
	# 	user = super(UserUpdateForm, self).save()
	# 	img = Image.open(user.profile_image.path)
	# 	if img.height > 250 or img.width > 250:
	# 		output_size = (250, 250)
	# 		img.thumbnail(output_size)
	# 		img.save(user.profile_image.path)

	# 	# return user
		
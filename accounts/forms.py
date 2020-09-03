from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, UsernameField
from django.utils.translation import ugettext_lazy as _
from PIL import Image


class BaseModelForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		kwargs.setdefault('label_suffix', '')
		super(BaseModelForm, self).__init__(*args, **kwargs)


class UserSignUpForm(BaseModelForm, UserCreationForm):

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


class UserUpdateForm(UserChangeForm):
	password = None
	readonly_fields = ('username', )#'date_joined')

	def __init__(self, *args, **kwargs):
		super(UserUpdateForm, self).__init__(*args, **kwargs)
		for field in self.readonly_fields:
			self.fields[field].disabled = True
			
	class Meta:
		model = get_user_model()
		fields = ('email', 'first_name', 'last_name') #'username', 'date_of_birth', 'profile_image' 'date_joined'
		widgets = {
			# 'username': forms.TextInput(attrs={
			# 	'class': 'read-only text-input-acc pfl-col__input-box'
			# }),
			'email': forms.EmailInput(attrs={
				'class': 'text-input-acc pfl-col__input-box'
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
			# 'date_of_birth': forms.DateInput(attrs={
			# 	'type': 'date',
			# 	'class': 'text-input-acc pfl-col__input-box'
			# })
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
		
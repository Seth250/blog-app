from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class UserUpdateForm(UserChangeForm):
	password = None
	# readonly_fields = ('username', )#'date_joined')
	readonly_fields = ('email', )

	# change order
	def __init__(self, *args, **kwargs):
		super(UserUpdateForm, self).__init__(*args, **kwargs)
		for field in self.readonly_fields:
			self.fields[field].disabled = True
			
	class Meta:
		model = get_user_model()
		fields = ('email', 'first_name', 'last_name' ) #'username', 'date_of_birth', 'profile_image' 'date_joined'
		widgets = {
			# 'username': forms.TextInput(attrs={
			# 	'class': 'read-only text-input-acc pfl-col__input-box'
			# }),
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
			# 'date_of_birth': forms.DateInput(attrs={
			# 	'type': 'date',
			# 	'class': 'text-input-acc pfl-col__input-box'
			# })
		}

	# def clean_image(self):
	# 	cleaned_data = super(UserUpdateForm, self).clean()
	# 	profile_image = cleaned_data['image']
	# 	print(profile_image)
	# 	if not profile_image:
	# 		return profile_image

	# 	img = Image.open(profile_image.file)
	# 	if img.height > 150 or img.width > 150:
	# 		output_size = (150, 150)
	# 		extension = img.format.lower()
	# 		img = img.resize(output_size, Image.LANCZOS)
	# 		profile_image.file = type(profile_image.file)()
	# 		img.save(profile_image.file, extension, optimize=True)

	# 	return profile_image
		
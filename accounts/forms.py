from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = get_user_model()
		fields = ('username', 'email', )

		# def clean_username(self):
		# 	cleaned_data = super().clean()
		# 	username = cleaned_data.get("username")
		# 	if username and self.model.objects.filter(username__iexact=username).exists():
		# 		self.add_error('username', 'This Username already exists')

		# 	return username 
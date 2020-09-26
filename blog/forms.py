from django import forms
from .models import Post, Comment


class BaseModelForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		kwargs.setdefault('label_suffix', '')
		return super(BaseModelForm, self).__init__(*args, **kwargs)


class PostForm(BaseModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'thumbnail')
        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'form-content'}
            )
        }


class CommentForm(BaseModelForm):

    class Meta:
        model = Comment
        fields = ('content', )
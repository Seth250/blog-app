from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'thumbnail')
        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'form-content'}
            )
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )
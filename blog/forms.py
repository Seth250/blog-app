from django import forms
from .models import Post, Comment
from PIL import Image


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'thumbnail')

    def clean_thumbnail(self):
        cleaned_data = super(PostForm, self).clean()
        thumbnail = cleaned_data['thumbnail']
        if not thumbnail:
            return thumbnail

        img = Image.open(thumbnail.file)
        if img.height > 375 or img.width > 500:
            output_size = (500, 375)
            extension = img.format.lower()
            img.thumbnail(output_size)
            thumbnail.file = type(thumbnail.file)()
            img.save(thumbnail.file, extension)

        return thumbnail


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )
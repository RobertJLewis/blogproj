from django import forms
from .models import Comment, Post


# Comment form: only text
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


# Quick post form: only text, no images/videos
class QuickPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Removed 'image' and any file fields

    def save(self, commit=True, user=None):
        post = super().save(commit=False)

        # Assign the user as the author
        if user:
            post.author = user

        if commit:
            post.save()
        return post

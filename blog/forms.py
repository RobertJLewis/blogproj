from django import forms
from .models import Comment, Post

# Existing comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


# Quick post form (like "What's on your mind?" box)
from django import forms
from .models import Post

class QuickPostForm(forms.ModelForm):
    media = forms.FileField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'image'] 

    def save(self, commit=True, user=None):
        post = super().save(commit=False)

        media = self.cleaned_data.get('media')
        if media:
            if media.content_type.startswith('image/'):
                post.image = media
                post.video = None
            elif media.content_type.startswith('video/'):
                post.video = media
                post.image = None

        if user:
            post.author = user

        if commit:
            post.save()
        return post
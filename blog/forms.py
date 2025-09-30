from django import forms
from .models import Comment, Post

# Existing comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# Quick post form (like "What's on your mind?" box)
class QuickPostForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': "What's on your mind?",
                'rows': 3,
                'class': 'form-control'
            }
        ),
        label=''
    )

    class Meta:
        model = Post
        fields = ['content']

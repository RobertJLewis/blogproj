from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm        
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post       
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import QuickPostForm

from django.views.generic import ListView
from django.shortcuts import redirect
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


    # def home(request):
    #     context = {
    #         'posts': Post.objects.all()
    #     }
    #     return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # optional, Django guesses by default

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()  # empty comment form
        return context
    
    def post(self, request, *args, **kwargs):
        """Handle a comment being posted."""
        self.object = self.get_object()  # current Post
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = self.object
            comment.save()
            return redirect(self.object.get_absolute_url())  # refresh page
        context = self.get_context_data(form=form)
        return self.render_to_response(context)




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
        # if self.request.user == post.author:
        #     return True
        # return False


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def post(self, request, *args, **kwargs):
        content = request.POST.get('content')
        if content:
            Post.objects.create(author=request.user, title=content[:50], content=content)
        return redirect('blog-home')


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Remove dislike if it exists
    if user in post.dislikes.all():
        post.dislikes.remove(user)

    # Toggle like
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return redirect(request.META.get('HTTP_REFERER', 'blog-home'))

@login_required
def dislike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Remove like if it exists
    if user in post.likes.all():
        post.likes.remove(user)

    # Toggle dislike
    if user in post.dislikes.all():
        post.dislikes.remove(user)
    else:
        post.dislikes.add(user)

    return redirect(request.META.get('HTTP_REFERER', 'blog-home'))


@login_required
def home(request):
    if request.method == 'POST':
        form = QuickPostForm(request.POST)
        if form.is_valid():
            quick_post = form.save(commit=False)
            quick_post.author = request.user
            quick_post.save()
            return redirect('blog-home')  # refresh page
    else:
        form = QuickPostForm()

    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'form': form,
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Comment.objects.create(author=request.user, post=post, content=content)
    return redirect('blog-home')
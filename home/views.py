from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/index.html', {'posts': posts})


class PostDetailView(View):
    def get(self, request, user_id, post_slug):
        user = get_object_or_404(User, pk=user_id)
        post = get_object_or_404(Post, user=user)
        return render(request, 'home/detail.html', {'post': post})


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.user.id == request.user.id:
            post.delete()
            messages.success(request, 'Delete successfully', 'success')
            return redirect('account:user_profile', request.user.id)
        else:
            messages.error(request, 'you cant delete this post', 'warning')
        return redirect('home:index')

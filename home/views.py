from django.shortcuts import render
from django.views import View
from .models import Post
from django.contrib.auth.models import User


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/index.html', {'posts': posts})


class PostDetailView(View):
    def get(self, request, user_id, post_slug):
        user = User.objects.get(pk=user_id)
        post = Post.objects.get(user=user)
        return render(request, 'home/detail.html', {'post': post})

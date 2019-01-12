from django.shortcuts import render
from webapp.models import User, UserInfo, Post
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    permission_required = 'webapp.view_order'



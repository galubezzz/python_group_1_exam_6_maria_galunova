from django.shortcuts import render
from webapp.models import User, UserInfo, Post
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from webapp.forms import PostForm

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('webapp:post_details', kwargs={'pk': self.object.pk})

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    template_name = 'post_update.html'
    form_class = CourseForm
    success_url = reverse_lazy('webapp:posts')
from django.shortcuts import render
from webapp.models import User, UserInfo, Post
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from webapp.forms import PostForm, UserForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return self.model.objects.order_by('-date')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:post_details', kwargs={'pk': self.object.pk})


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostForm
    success_url = reverse_lazy('webapp:posts')

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != self.request.user:
            return HttpResponseRedirect(reverse('webapp:post_details', kwargs={'pk': pk}))
        return super().get(request, pk=pk)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('webapp:posts')

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != self.request.user:
            return HttpResponseRedirect(reverse('webapp:post_details', kwargs={'pk': pk}))
        return super().get(request, pk=pk)

class UserDetailView(DetailView):
    model = UserInfo
    template_name = "user_details.html"


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserUpdateView(UpdateView):
    model = UserInfo
    template_name = 'user_update.html'
    form_class = UserForm
    success_url = reverse_lazy('webapp:user_details')
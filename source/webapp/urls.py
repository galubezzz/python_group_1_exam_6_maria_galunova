from django.urls import path
from webapp.views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView, UserListView, UserDetailView, UserUpdateView

app_name = 'webapp'

urlpatterns = [
    path('post/<int:pk>', PostDetailView.as_view(), name='post_details'),
    path('', PostListView.as_view(), name='posts'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('users', UserListView.as_view(), name='users'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_details'),
    path('user/<int:pk>/update', UserUpdateView.as_view(), name='user_update'),
]
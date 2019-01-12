from django.urls import path
from webapp.views import PostDetailView, PostListView, PostCreateView

app_name = 'webapp'

urlpatterns = [
    path('post/<int:pk>', PostDetailView.as_view(), name='post_details'),
    path('', PostListView.as_view(), name='posts'),
    path('post/create', PostCreateView.as_view(), name='post_create')
]
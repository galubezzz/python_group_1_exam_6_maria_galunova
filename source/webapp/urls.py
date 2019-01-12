from django.urls import path
from webapp.views import PostDetailView, PostListView

app_name = 'webapp'

urlpatterns = [
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='posts')
]
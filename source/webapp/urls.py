from django.urls import path
from webapp.views import PostDetailView

app_name = 'webapp'

urlpatterns = [
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
]
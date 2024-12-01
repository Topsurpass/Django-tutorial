from django.urls import path
from .views import PostDetailView, PostListCreateView

urlpatterns = [
    path('message/', PostListCreateView.as_view(), name='message-list-create'),
    path('message/<uuid:uuid>/', PostDetailView.as_view(), name='message-detail'),
]
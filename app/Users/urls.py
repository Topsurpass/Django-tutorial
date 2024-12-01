from django.urls import path
from .views import PostDetailView, PostListCreateView

urlpatterns = [
    path('user/', PostListCreateView.as_view(), name='user-list-create'),
    path('user/<slug:slug>/', PostDetailView.as_view(), name='user-detail'),
]
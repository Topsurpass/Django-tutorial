from django.urls import path
from .views import PostDetailView, PostListCreateView

urlpatterns = [
    path('review/', PostListCreateView.as_view(), name='review-list-create'),
    path('review/<uuid:pk>/', PostDetailView.as_view(), name='review-detail'),
]
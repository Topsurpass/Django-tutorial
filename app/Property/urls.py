from django.urls import path
from .views import PostDetailView, PostListCreateView

urlpatterns = [
    path('property/', PostListCreateView.as_view(), name='property-list-create'),
    path('property/<slug:slug>/', PostDetailView.as_view(), name='property-detail'),
]
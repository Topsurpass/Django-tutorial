from django.urls import path
from .views import PostDetailView, PostListCreateView

urlpatterns = [
    path('payment/', PostListCreateView.as_view(), name='payment-list-create'),
    path('payment/<uuid:uuid>/', PostDetailView.as_view(), name='payment-detail'),
]
from django.urls import path
from .views import PostDetailView, ListCreateView, PostCreateView, PostLoginView

urlpatterns = [
    path('user/', ListCreateView.as_view(), name='user-list'),
    path('auth/signup/', PostCreateView.as_view(), name='user-create'),
    path('auth/login/', PostLoginView.as_view(), name='user-login'),
    path('user/<slug:slug>/', PostDetailView.as_view(), name='user-detail'),
]
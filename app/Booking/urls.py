from django.urls import path
from .views import PostDetailView, PostListCreateView

urlpatterns = [
    path('booking/', PostListCreateView.as_view(), name='booking-list-create'),
    path('booking/<uuid:booking_id>/', PostDetailView.as_view(), name='booking-detail'),
]
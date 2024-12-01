from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Review	
from .serializers import ReviewSerializer

class PostListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

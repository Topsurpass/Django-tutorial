from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User	
from .serializers import UserSerializer

class PostListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'slug'


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'slug'

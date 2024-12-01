from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Property	
from .serializers import PropertySerializer

class PostListCreateView(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'slug'


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'slug'

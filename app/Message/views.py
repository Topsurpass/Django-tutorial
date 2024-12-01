from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Message	
from .serializers import MessageSerializer

class PostListCreateView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Payment	
from .serializers import PaymentSerializer

class PostListCreateView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

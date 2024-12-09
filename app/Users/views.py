from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class ListCreateView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'slug'
    
class PostCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class PostLoginView(CreateAPIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        serializer_class = LoginSerializer(data=data)
        if not serializer_class.is_valid():
            return Response({
                "status": False,
                "data": serializer_class.errors
            })
        email = serializer_class.data['email']
        password = serializer_class.data['password']        
        user = authenticate(request, username=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            user_details = User.objects.filter(email=email).values(
                'user_id', 'email', 'first_name', 'last_name', 'role',
            ).first()
            
            return Response({
                "status": True,
                "message": "Login successful",
                "token": token.key,
                "user": user_details
            })
        return Response({
            "status": False,
            "message": "Invalid email or password"
        }, status=401)

        

class PostDetailView(RetrieveUpdateDestroyAPIView):
    #permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'slug'
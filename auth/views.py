from django.contrib.auth.models import User
from .serializers import MyTokenObtainPairSerializer,RegisterSerializer,ChangePasswordSerializer,UpdateUserSerializer
from rest_framework import generics,status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken,OutstandingToken,BlacklistedToken
from rest_framework.views import APIView



# Create your views here.
class LogoutAllView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        tokens = OutstandingToken.objects.filter(user_id = request.user.id)
        for token in tokens:
            t,_ = BlacklistedToken.objects.get_or_create(token=token)
        return Response(status=status.HTTP_205_RESET_CONTENT)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT) 
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateUserSerializer

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    
    
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer
    
    

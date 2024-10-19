from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer


User = get_user_model()

class UserSignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

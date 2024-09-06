# users/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, Admin, Owner
from rest_framework import serializers
from .serializers import CustomUserSerializer, AdminnSerializer, OwnerSerializer, TokenSerializer,ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import status
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdmin


class SignUpView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user_type = request.data.get('user_type')

        
        if user_type == 'admin':
            serializer = AdminnSerializer(data=request.data)
        elif user_type == 'owner':
            if not request.user.is_authenticated or not request.user.is_staff:
                return Response({"detail": "Only admins can create owners."}, status=status.HTTP_403_FORBIDDEN)
            serializer = OwnerSerializer(data=request.data)
        else:
            serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        
        # print("Validated Data:", validated_data)
        return Response(validated_data)
    




class ChangePasswordView(generics.UpdateAPIView):
    serializer_class=ChangePasswordSerializer
    permission_classes=[IsAuthenticated]


    def patch(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_password = serializer.validated_data.get('new_password')
        
        user.set_password(new_password)
        user.save()
        return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)


    



    



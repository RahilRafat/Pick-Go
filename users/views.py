from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer, TokenSerializer,ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken
from .permissions import IsAdmin
from rest_framework.views import APIView
from .models import CustomUser


class SignUpView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user_type = request.data.get('user_type')
        user = request.user

        serializer = CustomUserSerializer(data=request.data)

        if user_type == 'owner':
            if not user.is_authenticated or not user.is_staff:
                return Response({"detail": "You do not have permission to create this type of user."}, status=status.HTTP_403_FORBIDDEN)
        
       
        if serializer.is_valid():
            new_user = serializer.save()
            refresh = RefreshToken.for_user(new_user)
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

        
      
        return Response(validated_data)
    




class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data.get('password')
        new_password = serializer.validated_data.get('new_password')

       
        if not  user.check_password(password):
            return Response({"detail": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)

        
        user.set_password(new_password)
        user.save()

        return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)


    def get_serializer(self, *args, **kwargs):
        from rest_framework import serializers

        class PasswordChangeSerializer(serializers.Serializer):
            password = serializers.CharField(write_only=True)
            new_password = serializers.CharField(write_only=True)

        return PasswordChangeSerializer(*args, **kwargs)


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin] 

    


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        
        refresh_token = request.data.get('refresh')

        if refresh_token is None:
            return Response({'detail': 'Refresh token is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
           
            token = RefreshToken(refresh_token)
            token.blacklist() 
        except InvalidToken:
            return Response({'detail': 'Invalid refresh token.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_205_RESET_CONTENT)
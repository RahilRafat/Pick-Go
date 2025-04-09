from django.urls import path
from .views import SignUpView, LoginView,PasswordChangeView,UserListView,LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('changepassword/', PasswordChangeView.as_view(), name='change_password'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('logout/',LogoutView.as_view(),name='logout')
    
]

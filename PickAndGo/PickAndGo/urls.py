"""
URL configuration for PickAndGo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
       title="Pick-Up Service API",
       default_version='v1',
       description="This API allows users to manage pick-up services, including scheduling, updating status, and user management.",
       terms_of_service="https://www.pickupservice.com/terms/",
       contact=openapi.Contact(email="support@pickupservice.com"),
       license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('resturant/',include('restaurant.urls')),
    path('food/',include('food.urls')),
    path('size/',include('sizes.urls')),
    path('users/',include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  
   
    path('subprice/',include('supreceipt.urls')),
    path('reciept/',include('totalreceipt.urls')),
    path('pickup/',include('pickup.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

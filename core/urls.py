"""
URL configuration for core project.

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

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static
from user_auth.views import login

schema_view = get_schema_view (
    openapi.Info(
            title='Learning center api',
            default_version='v1',
            description='Learning center demo project',
            terms_of_service='demo.com',
            contact=openapi.Contact(email='ramazonof07@gmail.com'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),

    path('teachers/', include('teachers.urls')),
    path('courses/', include('courses.urls')),
    path('results/', include('results.urls')),
    path('enrolment/', include('enrolment.urls')),
    path('user/', include('user_auth.urls')),

    path('auth/', include('social_django.urls',namespace='social')),
    path('login/',login,name='login'),
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

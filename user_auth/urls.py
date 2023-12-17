from .views import ObtainTokenView
from django.urls import path

urlpatterns = [
    path('token/',ObtainTokenView.as_view())
]

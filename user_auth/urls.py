from .views import ObtainTokenView,Registerserializer
from django.urls import path

urlpatterns = [
    path('token/',ObtainTokenView.as_view()),
    path('register/',Registerserializer.as_view()),
]

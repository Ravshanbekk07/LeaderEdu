from .views import ObtainTokenView,RegisterView,LoginView,LogoutView,PasswordChange#,GoogleSignUp
from django.urls import path

urlpatterns = [
    path('token/',ObtainTokenView.as_view()),
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('change-password/',PasswordChange.as_view()),
    # path('auth/google/',GoogleSignup.as_view(),name='social_signup'),
    
]

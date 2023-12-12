from django.urls import path
from .views import CourseList

urlpatterns = [
    path('all/',CourseList.as_view()),
    
]

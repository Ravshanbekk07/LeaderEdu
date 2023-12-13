from django.urls import path
from .views import CourseList,CategoryList,CategoryDelete

urlpatterns = [
    path('all/',CourseList.as_view()),
    path('category/all/',CategoryList.as_view()),
    path('category/<int:pk>/',CategoryDelete.as_view()),
    
]

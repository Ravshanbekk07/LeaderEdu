from django.urls import path
from .views import CourseList,CourseDetail,CourseCreate,CourseDelete,CourseUpdate,CategoryList,CategoryDelete

urlpatterns = [
    path('all/',CourseList.as_view()),
    path('detail/<int:pk>/',CourseDetail.as_view()),
    path('create/',CourseCreate.as_view()),
    path('update/<int:pk>/',CourseUpdate.as_view()),
    path('delete/<int:pk>/',CourseDelete.as_view()),


    path('category/all/',CategoryList.as_view()),
    path('category/<int:pk>/',CategoryDelete.as_view()),
    
]

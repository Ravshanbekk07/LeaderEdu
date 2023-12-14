from django.urls import path
from .views import TeacherList,TeacherDetail

urlpatterns = [
    path('all/',TeacherList.as_view()),
    path('<int:pk>/',TeacherDetail.as_view())
]


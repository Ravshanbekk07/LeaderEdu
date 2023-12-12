from django.urls import path
from .views import TeacherList,TeacherDElete

urlpatterns = [
    path('all/',TeacherList.as_view()),
    path('<int:pk>/',TeacherDElete.as_view())
]


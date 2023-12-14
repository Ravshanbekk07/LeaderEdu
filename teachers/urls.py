from django.urls import path
from .views import TeacherList,TeacherDetail,TeacherSearch

urlpatterns = [
    path('all/',TeacherList.as_view()),
    path('<int:pk>/',TeacherDetail.as_view()),
    path('search/',TeacherSearch.as_view()),
]


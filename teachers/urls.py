from django.urls import path
from .views import TeacherList,TeacherDetail,TeacherSearch,TeacherCreateView,TeacherDelete,TeacherUpdate

urlpatterns = [
    path('all/',TeacherList.as_view()),
    path('create/',TeacherCreateView.as_view()),
    path('detail/<int:pk>/',TeacherDetail.as_view()),
    path('delete/<int:pk>/',TeacherDelete.as_view()),
    path('update/<int:pk>/',TeacherUpdate.as_view()),
    
    path('search/',TeacherSearch.as_view()),
]


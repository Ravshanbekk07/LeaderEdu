from django.urls import path
from .views import EnrolmentDelete,EnrolmentDetail,EnrolmentList,EnrolmentUpdate,EnrolmentCreate

urlpatterns = [
    path('all/',EnrolmentList.as_view()),
    path('detail/<int:pk>/',EnrolmentDetail.as_view()),
    path('delete/<int:pk>/',EnrolmentDelete.as_view()),
    path('update/<int:pk>/',EnrolmentUpdate.as_view()),
    path('create/',EnrolmentCreate.as_view()),
]

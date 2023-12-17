from django.urls import path
from .views import EnrolmentDelete,EnrolmentDetail,EnrolmentList,EnrolmentUpdate

urlpatterns = [
    path('all/',EnrolmentList.as_view())
]

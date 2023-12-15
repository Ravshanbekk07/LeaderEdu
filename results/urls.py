from django.urls import path
from .views import ResultList,ResultCreate,ResultDetail,ResultUpdate,ResultDelete

urlpatterns = [
    path('all/',ResultList.as_view()),
    path('create/',ResultCreate.as_view()),
    path('detail/<int:pk>/',ResultDetail.as_view()),
    path('update/<int:pk>/',ResultUpdate.as_view()),
    path('delete/<int:pk>/',ResultDelete.as_view()),
]


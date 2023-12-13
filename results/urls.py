from django.urls import path
from .views import ResultList

urlpatterns = [
    path('all/',ResultList.as_view())
]


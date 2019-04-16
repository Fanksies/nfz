from django.urls import path
from .views import PhotoDetail, PhotoList


urlpatterns = [
    path('', PhotoList.as_view(), name='photo_list'),
    path('<slug:slug>/', PhotoDetail.as_view(), name='photo_detail'),
]
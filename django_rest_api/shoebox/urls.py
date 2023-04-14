from django.urls import path
from . import views

urlpatterns = [
    path('shoes', views.ShoesList.as_view(), name='shoes_list'),
    path('shoes/<int:pk>', views.ShoesDetail.as_view(), name='shoes_detail'),
]
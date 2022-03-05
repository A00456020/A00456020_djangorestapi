from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("hotels_list/", views.Hotels_list, name="listofhotels"),
    path("hotels_list/<str:pk>", views.Hotels_detail, name="detailsofhotels"),
    path("delete_hotel/<str:pk>", views.Delete_Hotel, name="deletehotel")

]
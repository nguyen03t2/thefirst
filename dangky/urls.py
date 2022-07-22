from django.contrib import admin
from django.urls import path
from dangky import views

urlpatterns = [
    path('', views.dangky),
    path('xulydangky', views.xulydangky, name="xulydangky"),
]


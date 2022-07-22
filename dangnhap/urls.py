from django.contrib import admin
from django.urls import path
from dangnhap import views

urlpatterns = [
    
    path('', views.dangnhap),
    path('xuly_dangnhap', views.xuly_dangnhap, name="xuly_dangnhap"),
    path('themnhanvien', views.themnhanvien, name="themnhanvien"),
     path('dsnhanvien', views.dsnhanvien, name="dsnhanvien"),
    path('xuly_themnhanvien', views.xuly_themnhanvien, name="xuly_themnhanvien"),
    path('chitiet/<int:nhanvien_id>/',views.chi_tiet,name="chi_tiet"),
    path('xuly_capnhatnv',views.xuly_capnhatnv,name="xuly_capnhatnv"),
    path('xoa/<int:nhanvien_id>',views.xoa_nv,name="xoa_nv"),
]
import email
from django.db import models

# Create your models here.

class NguoiDung(models.Model):
    ten_dang_nhap = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mat_khau = models.CharField(max_length=100)

    def __str__(self):
        return self.ten_dang_nhap

class NhanVien(models.Model):
    ho_ten = models.CharField(max_length=100)
    chuc_vu = models.CharField(max_length=100)
    nam_sinh = models.IntegerField()
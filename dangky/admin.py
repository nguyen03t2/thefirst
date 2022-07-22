from django.contrib import admin
from dangky.models import NguoiDung
from dangky.models import NhanVien

# Register your models here.
class NguoiDungAdmin(admin.ModelAdmin):
    list_display = ('ten_dang_nhap','email','mat_khau')
    list_display_links = ('ten_dang_nhap','email')
    list_filter = ('ten_dang_nhap','email')
    search_fields = ('ten_dang_nhap','email')
    list_per_page: 25

admin.site.register(NguoiDung, NguoiDungAdmin)

class NhanVienAdmin(admin.ModelAdmin):
    list_display = ('ho_ten','chuc_vu','nam_sinh')
    list_display_links = ('ho_ten','chuc_vu')
    list_filter = ('ho_ten','chuc_vu')
    search_fields = ('ho_ten','chuc_vu','nam_sinh')
    list_per_page: 25

admin.site.register(NhanVien, NhanVienAdmin)
from gc import get_objects
from django.shortcuts import render, get_object_or_404
from dangky.models import NguoiDung, NhanVien

# Create your views here.
def dangnhap(request):
    return render(request,'dangnhap.html')

def xuly_dangnhap(request):
    ten = request.GET.get('ten')
    mk = request.GET.get('mk')

    thongtin = NguoiDung.objects.filter(ten_dang_nhap=ten, mat_khau=mk)
    danh_sach = NguoiDung.objects.all()
    danh_sachnv = NhanVien.objects.all()

    context = {
        'ds_nhanvien':danh_sachnv,
        'ds_nguoidung':danh_sach
    }
    if (thongtin.exists()):
        return render(request,'danhsach.html',context)
    else:
        return render(request,'loi.html')

def themnhanvien(request):
    return render(request,'themnhanvien.html')

def dsnhanvien(request):
    danh_sachnv = NhanVien.objects.all()
    context = {
        'ds_nhanvien':danh_sachnv
    }
    return render(request,'danhsach.html',context)

def xuly_themnhanvien(request):
    ten = request.GET.get('ten')
    chucvu = request.GET.get('chucvu')
    namsinh = request.GET.get('namsinh')
    dulieu = NhanVien(
            ho_ten = ten,
            chuc_vu = chucvu,
            nam_sinh = namsinh
        )
    dulieu.save()
    return render(request,'themnhanvien.html')

def chi_tiet(request,nhanvien_id):
    nhan_vien = get_object_or_404(NhanVien, pk=nhanvien_id)
    return render(request,'chitiet.html',{'nv':nhan_vien})
    
def xuly_capnhatnv(request):
    ten = request.GET.get('ten')
    chucvu = request.GET.get('chucvu')
    namsinh = request.GET.get('namsinh')
    id_nv = request.GET.get('id_nv')
    
    NhanVien.objects.filter(id=id_nv).update(
        ho_ten = ten,
        chuc_vu = chucvu,
        nam_sinh = namsinh
    )
    danh_sachnv = NhanVien.objects.all()
    context = {
        'ds_nhanvien':danh_sachnv
    }
    return render(request,'danhsach.html',context)

def xoa_nv(request,nhanvien_id):
    dulieu = get_object_or_404(NhanVien, pk=nhanvien_id)
    try:
        dulieu.delete()
    except:
        print("Xoa bi loi!")
    danh_sachnv = NhanVien.objects.all()
    context = {
        'ds_nhanvien':danh_sachnv
    }
    return render(request,'danhsach.html',context)
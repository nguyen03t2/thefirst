from django.shortcuts import render

from dangky.models import NguoiDung, NhanVien

# Create your views here.

def dangky(request):
    return render(request,'dangky.html')

def trangchu(request):
    return render(request,'trangchu.html')

def xulydangky(request):
    ten = request.GET.get('ten')
    email = request.GET.get('email')
    mk = request.GET.get('matkhau')

    if (len(ten)>4 and ('@' in email)):
        dulieu = NguoiDung(
            ten_dang_nhap = ten,
            email = email,
            mat_khau = mk
        )
        dulieu.save()
        return render(request,'dangnhap.html')
    else:
        return render(request,'Error.html')


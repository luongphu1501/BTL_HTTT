from django.shortcuts import render
from django.views import View
from django.http import request
from .models import Benh, TrieuChung
from .ultils import cbr
# Create your views here.

def TrangChu(request):
    benh = Benh.objects.all()[0];
    list_tc = benh.trieuchung_set.all().order_by("ki_hieu")
    context = {"list_tc": list_tc}
    return render(request, "TrangChu.html", context)

def KetQua(request):
    vote = {
    'p01' : request.POST['p01'],
    'p02' : request.POST['p02'],
    'p03' : request.POST['p03'],
    'p04' : request.POST['p04'],
    'p05' : request.POST['p05'],
    'p06' : request.POST['p06'],
    'p07' : request.POST['p07'],
    'p08' : request.POST['p08'],
    'p09' : request.POST['p09'],
    'p10' : request.POST['p10'],
    'p11' : request.POST['p11'],
    'p12' : request.POST['p12'],
    'p13' : request.POST['p13'],
    'p14' : request.POST['p14'],
    'p15' : request.POST['p15'],
    'p16' : request.POST['p16'],
    'p17' : request.POST['p17'],
    'p18' : request.POST['p18'],
    'p19' : request.POST['p19'],
    'p20' : request.POST['p20'],
    'p21' : request.POST['p21'],
    'p22' : request.POST['p22'],
    'p23' : request.POST['p23'],
    'p24' : request.POST['p24']
    }
    list_kq = []
    for value in vote.values():
        list_kq.append(float(value))
    index = cbr(list_kq)
    context = {"result": Benh.objects.get(pk = index)}
    return render(request, "KetQua.html", context)


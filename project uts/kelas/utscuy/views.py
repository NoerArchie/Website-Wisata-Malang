from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render 
from utscuy.models import Barang
from utscuy.models import Transaksi

def coba1(request):
    return HttpResponse('Welcome')

def home(request):
    title="Index"
    setTitle = {
        'titel':title,
    }
    return render(request,'index.html',setTitle)
# Create your views here.

def Barang_View(request):
    barangs= Barang.objects.all()
    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def Barang_Book(request):
    transaksis= Transaksi.objects.all()
    konteks={
        'transaksis':transaksis,
    }
    return render(request,'tampil_booking.html',konteks)


def produk(request):
    titelnya= 'produk'
    konteks = {
        'titel' : titelnya,
    }
    return render(request,'produk.html',konteks)

def about1(request):
    return render (request, 'about.html')



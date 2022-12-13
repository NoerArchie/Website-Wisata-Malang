from django.contrib import admin
from .models import Barang ,Jenis , Detailtrans, Transaksi


admin.site.register(Barang)
admin.site.register(Detailtrans)
admin.site.register(Jenis)
admin.site.register(Transaksi)
# Register your models here.

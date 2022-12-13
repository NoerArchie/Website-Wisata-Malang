# Create your models here.
from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodewisata=models.CharField(max_length=8)
    nama_wisata=models.CharField(max_length=50)
    harga_tiket=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    hari_kerja=models.CharField(max_length=50)
    jenis_wisata= models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "{}. {}. {}. {}. {}.".format(self.kodewisata,self.nama_wisata,self.harga_tiket,self.hari_kerja,self.jenis_wisata)

class Transaksi(models.Model):
    kodewisata=models.CharField(max_length=8)
    nama_pengunjung=models.CharField(max_length=50)
    jumlah_tiket=models.IntegerField()
    tanggal_keberangkatan=models.DateTimeField(auto_now_add=True)
    total=models.BigIntegerField()
        
    def __str__(self):
        return self.kodewisata

class Detailtrans(models.Model):
    kodetrans=models.CharField(max_length=10)
    kodebrg=models.CharField(max_length=8)
    qty=models.IntegerField()
    subtotal=models.BigIntegerField()

    def __str__(self):
        return "{}. {}".format(self.kodetrans,self.kodebrg)
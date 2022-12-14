# Generated by Django 4.1.3 on 2022-11-24 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detailtrans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodetrans', models.CharField(max_length=10)),
                ('kodebrg', models.CharField(max_length=8)),
                ('qty', models.IntegerField()),
                ('subtotal', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('ket', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodewisata', models.CharField(max_length=8)),
                ('nama_pengunjung', models.CharField(max_length=50)),
                ('jumlah_tiket', models.IntegerField()),
                ('tanggal_keberangkatan', models.DateTimeField(auto_now_add=True)),
                ('total', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodewisata', models.CharField(max_length=8)),
                ('nama_wisata', models.CharField(max_length=50)),
                ('harga_tiket', models.BigIntegerField()),
                ('link_gbr', models.CharField(blank=True, max_length=150)),
                ('hari_kerja', models.CharField(max_length=50)),
                ('jenis_wisata', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='utscuy.jenis')),
            ],
        ),
    ]

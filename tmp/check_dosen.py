import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'si_unh.settings')
django.setup()

from core.models import Dosen

dtpr_count = Dosen.objects.filter(kategori='dtpr').count()
tetap_count = Dosen.objects.filter(kategori='tetap').count()
lb_count = Dosen.objects.filter(kategori='luar_biasa').count()

print(f"DTPR count: {dtpr_count}")
print(f"Tetap count: {tetap_count}")
print(f"LB count: {lb_count}")

for d in Dosen.objects.filter(kategori='dtpr'):
    print(f"- {d.nama} ({d.kategori})")

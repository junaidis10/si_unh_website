from django.urls import path
from . import views

app_name = 'layanan_akademik'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    
    # Kerja Praktek / Magang
    path('mahasiswa/import/', views.MahasiswaImportView.as_view(), name='mahasiswa_import'),
    path('kp-magang/', views.KPListView.as_view(), name='kp_list'),
    path('kp-magang/pengajuan/', views.KPCreateView.as_view(), name='kp_create'),
    
    # Tugas Akhir
    path('tugas-akhir/', views.TAListView.as_view(), name='ta_list'),
    path('tugas-akhir/pendaftaran/', views.TACreateView.as_view(), name='ta_create'),
    
    # Penjadwalan
    path('jadwal/', views.JadwalView.as_view(), name='jadwal'),
]

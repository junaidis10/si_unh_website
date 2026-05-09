# SI UNH Website URL Configuration (Updated)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('Js0312yA11/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    # Public URLs
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('riset-publikasi/<str:tipe>/', views.riset_publikasi, name='riset_publikasi'),
    path('akademik/', views.akademik, name='akademik'),
    path('kurikulum/', views.kurikulum, name='kurikulum'),
    path('akreditasi/', views.akreditasi, name='akreditasi'),
    path('kemahasiswaan/', views.kemahasiswaan, name='kemahasiswaan'),
    path('layanan/', views.layanan, name='layanan'),
    path('survey/', views.survey_view, name='survey_view'),
    path('survey/pengguna/', views.submit_survey_lulusan, name='submit_survey_lulusan'),
    path('survey/kurikulum/', views.submit_survey_kurikulum, name='submit_survey_kurikulum'),
    path('survey/pengguna/export/', views.export_survey_excel, name='export_survey_excel'),
    path('survey/pengguna/import/', views.SurveyImportView.as_view(), name='survey_import'),
    path('survey/pengguna/stats/', views.survey_stats_view, name='survey_stats_view'),
    path('survey/kurikulum/stats/', views.kurikulum_stats_view, name='kurikulum_stats_view'),
    path('survey/vmts/export/', views.export_vmts_excel, name='export_vmts_excel'),
    path('survey/vmts/stats/', views.vmts_stats_view, name='vmts_stats_view'),
    path('submit-publikasi/', views.submit_publikasi, name='submit_publikasi'),
    path('media-informasi/', views.media_informasi, name='media_informasi'),
    
    # News & Documents
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('documents/<slug:slug>/', views.documents_by_category, name='documents_by_category'),
    path('download/<int:doc_id>/', views.download_document, name='download_document'),
    
    # Search
    path('search/', views.search, name='search'),
    
    # Repository Berkas
    path('repository-berkas/', views.repository_berkas, name='repository_berkas'),
    path('repository-berkas/download/<int:berkas_id>/', views.download_berkas, name='download_berkas'),
    
    # Authentication
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Admin Tools
    path('admin-tools/import-jadwal/', views.import_jadwal_excel, name='import_jadwal_excel'),
    path('admin-tools/import-penelitian/', views.import_penelitian, name='import_penelitian'),
    path('admin-tools/tarik-sinta/<int:dosen_id>/', views.tarik_sinta, name='tarik_sinta'),
    
    # Layanan Akademik (dikonsolidasi ke core)
    path('layanan-akademik/', views.LADashboardView.as_view(), name='la_dashboard'),
    path('layanan-akademik/mahasiswa/import/', views.MahasiswaImportView.as_view(), name='la_mahasiswa_import'),
    path('layanan-akademik/kp-magang/', views.KPListView.as_view(), name='la_kp_list'),
    path('layanan-akademik/kp-magang/pengajuan/', views.KPCreateView.as_view(), name='la_kp_create'),
    path('layanan-akademik/kp-magang/detail/', views.KPDetailView.as_view(), name='la_kp_detail'),
    path('layanan-akademik/tugas-akhir/', views.TAListView.as_view(), name='la_ta_list'),
    path('layanan-akademik/tugas-akhir/pendaftaran/', views.TACreateView.as_view(), name='la_ta_create'),
    path('layanan-akademik/tugas-akhir/detail/', views.TADetailView.as_view(), name='la_ta_detail'),
    path('layanan-akademik/tugas-akhir/<int:pk>/edit/', views.TAUpdateView.as_view(), name='la_ta_update'),
    path('layanan-akademik/tugas-akhir/pendaftaran-sidang/', views.SidangCreateView.as_view(), name='la_sidang_create'),
    path('layanan-akademik/judul-proposal/', views.JudulProposalCreateView.as_view(), name='la_judul_proposal_create'),
    path('layanan-akademik/jadwal/', views.LAJadwalView.as_view(), name='la_jadwal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # Production: tetap serve media via Django jika belum ada Nginx/Apache
    # Untuk performa optimal, gunakan whitenoise atau konfigurasi web server
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin site customization
admin.site.site_header = "Program Studi Sistem Informasi UNH Administrasi"
admin.site.site_title = "Program Studi Sistem Informasi UNH Administrasi"
admin.site.index_title = "Welcome to Program Studi Sistem Informasi UNH Administrasi"


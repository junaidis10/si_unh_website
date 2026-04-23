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
    path('akademik/', views.akademik, name='akademik'),
    path('kurikulum/', views.kurikulum, name='kurikulum'),
    path('akreditasi/', views.akreditasi, name='akreditasi'),
    path('kemahasiswaan/', views.kemahasiswaan, name='kemahasiswaan'),
    path('layanan/', views.layanan, name='layanan'),
    path('survey/', views.survey_view, name='survey_view'),
    path('survey/pengguna/', views.submit_survey_lulusan, name='submit_survey_lulusan'),
    path('survey/kurikulum/', views.submit_survey_kurikulum, name='submit_survey_kurikulum'),
    path('survey/pengguna/export/', views.export_survey_excel, name='export_survey_excel'),
    path('survey/pengguna/stats/', views.survey_stats_view, name='survey_stats_view'),
    path('survey/kurikulum/stats/', views.kurikulum_stats_view, name='kurikulum_stats_view'),
    path('survey/vmts/export/', views.export_vmts_excel, name='export_vmts_excel'),
    path('survey/vmts/stats/', views.vmts_stats_view, name='vmts_stats_view'),
    path('media-informasi/', views.media_informasi, name='media_informasi'),
    
    # News & Documents
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('documents/<slug:slug>/', views.documents_by_category, name='documents_by_category'),
    path('download/<int:doc_id>/', views.download_document, name='download_document'),
    
    # Search
    path('search/', views.search, name='search'),
    
    # Authentication
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Admin Tools
    path('admin-tools/import-jadwal/', views.import_jadwal_excel, name='import_jadwal_excel'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin site customization
admin.site.site_header = "Program Studi Sistem Informasi UNH Administrasi"
admin.site.site_title = "Program Studi Sistem Informasi UNH Administrasi"
admin.site.index_title = "Welcome to Program Studi Sistem Informasi UNH Administrasi"

# Struktur Project SI UNH Website

```
si_unh_website/
│
├── si_unh/                      # Django Project Settings
│   ├── __init__.py
│   ├── settings.py              # Konfigurasi utama Django
│   ├── urls.py                  # URL routing utama
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
│
├── core/                        # Main Application
│   ├── __init__.py
│   ├── admin.py                 # Admin panel configuration
│   ├── apps.py                  # App configuration
│   ├── models.py                # Database models (16 models)
│   └── views.py                 # View functions
│
├── templates/                   # HTML Templates
│   ├── base.html                # Base template (navbar, footer)
│   ├── home.html                # Homepage dengan slider
│   ├── profile.html             # Visi, Misi, Prospek
│   ├── akademik.html            # Data Dosen
│   ├── kurikulum.html           # Dokumen Kurikulum
│   ├── akreditasi.html          # Sertifikat Akreditasi
│   ├── kemahasiswaan.html       # Prestasi & Alumni
│   ├── layanan.html             # Link layanan & Job Career
│   ├── media_informasi.html     # Berita & Gallery
│   └── login.html               # Login admin
│
├── media/                       # User Uploaded Files
│   ├── slides/                  # Slider images
│   ├── sambutan/                # Foto ketua prodi
│   ├── dosen/                   # Foto dosen
│   ├── news/                    # Thumbnail berita
│   ├── gallery/                 # Gallery photos
│   ├── documents/               # Uploaded documents
│   ├── akreditasi/              # Sertifikat akreditasi
│   ├── prestasi/                # Foto prestasi
│   └── alumni/                  # Foto alumni
│
├── static/                      # Static Files (CSS, JS, Images)
│   └── (files collected by collectstatic)
│
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (create this)
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore file
│
├── README.md                    # Project documentation
├── PANDUAN_INSTALASI.md         # Installation guide
├── STRUKTUR_PROJECT.md          # This file
├── database_schema.sql          # SQL schema & sample data
│
├── setup_project.bat            # Auto setup script (Windows)
└── run_server.bat               # Run development server (Windows)
```

## Database Models (16 Tables)

1. **Slide** - Homepage slider
2. **Sambutan** - Sambutan Ketua Prodi
3. **VisiMisi** - Visi & Misi
4. **ProspekKeunggulan** - Prospek Lulusan
5. **Dosen** - Data Dosen (Tetap & Luar Biasa)
6. **DocumentCategory** - Kategori Dokumen
7. **Document** - Dokumen (upload/download)
8. **News** - Berita
9. **Gallery** - Gallery Foto & Video
10. **Prestasi** - Prestasi Mahasiswa
11. **Penelitian** - Penelitian & Pengabdian
12. **Akreditasi** - Sertifikat Akreditasi
13. **Alumni** - Data Alumni
14. **JobCareer** - Lowongan Pekerjaan
15. **Link** - Link Eksternal (SIAKAD, V-Class, dll)
16. **PageContent** - Konten Halaman Statis

## URL Routes

| URL | View | Template | Description |
|-----|------|----------|-------------|
| / | home | home.html | Homepage |
| /profile/ | profile | profile.html | Visi & Misi |
| /akademik/ | akademik | akademik.html | Dosen |
| /kurikulum/ | kurikulum | kurikulum.html | Kurikulum |
| /akreditasi/ | akreditasi | akreditasi.html | Akreditasi |
| /kemahasiswaan/ | kemahasiswaan | kemahasiswaan.html | Prestasi & Alumni |
| /layanan/ | layanan | layanan.html | Layanan |
| /media/ | media_informasi | media_informasi.html | Berita & Gallery |
| /admin/ | Django Admin | (built-in) | Admin Panel |
| /login/ | user_login | login.html | Login |

## Features Checklist

### ✅ Homepage
- [x] Dynamic slider
- [x] Sambutan Ketua Prodi
- [x] Quick stats
- [x] Latest news
- [x] Gallery preview

### ✅ Profile Prodi
- [x] Visi & Misi
- [x] Prospek Lulusan
- [x] Keunggulan

### ✅ Akademik
- [x] Dosen Tetap
- [x] Dosen Luar Biasa
- [x] Profile lengkap (foto, NIDN, email, etc)
- [x] Link Scholar/Scopus/SINTA

### ✅ Kurikulum
- [x] Kurikulum OBE K22 (upload/download)
- [x] Kurikulum KKNI K17 (upload/download)
- [x] Dynamic documents

### ✅ Akreditasi
- [x] Sertifikat Akreditasi
- [x] Laporan Evaluasi Diri (LED)
- [x] LKPS
- [x] Upload/Download documents

### ✅ Kemahasiswaan & Alumni
- [x] Prestasi Mahasiswa
- [x] Data Alumni
- [x] Buku Panduan

### ✅ Layanan
- [x] Link SIAKAD, V-Class, OJS
- [x] Pembimbing (PA, Seminar, Skripsi)
- [x] Job Career
- [x] Penelitian & Pengabdian

### ✅ Media & Informasi
- [x] Berita (dengan view counter)
- [x] Gallery Foto
- [x] Gallery Video

### ✅ Admin Features
- [x] Upload/Download semua dokumen
- [x] Management konten
- [x] User authentication

## Technology Stack

- **Backend**: Django 5.0.1
- **Frontend**: Tailwind CSS (CDN)
- **Database**: MySQL (XAMPP)
- **Rich Text**: CKEditor
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Poppins)

## Color Scheme

- **Primary (Ungu)**: #7e22ce to #581c87
- **Gold (Emas)**: #f59e0b to #78350f
- **Gradient**: Linear gradient purple to gold

## Responsive Breakpoints

- Mobile: < 768px
- Tablet: 768px - 1023px
- Desktop: >= 1024px

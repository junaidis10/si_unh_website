# 📁 SI UNH Website - Index File

## 📋 Daftar File dan Direktori

### 🔧 Core Django Files
```
manage.py                    # Django management script
requirements.txt             # Python dependencies
.env.example                 # Environment variables template
.gitignore                   # Git ignore rules
```

### ⚙️ Configuration Files
```
si_unh/
├── __init__.py             # Python package init
├── settings.py             # Django settings (database, apps, middleware)
├── urls.py                 # Main URL routing
├── wsgi.py                 # WSGI configuration
└── asgi.py                 # ASGI configuration
```

### 📦 Core Application
```
core/
├── __init__.py             # App init
├── admin.py                # Admin panel configuration (16 models)
├── apps.py                 # App configuration
├── models.py               # Database models (16 tables)
└── views.py                # View functions (15+ views)
```

### 🎨 Templates (HTML)
```
templates/
├── base.html               # Base template (navbar, footer, Tailwind)
├── home.html               # Homepage (slider, sambutan, news, gallery)
├── profile.html            # Visi & Misi, Prospek
├── akademik.html           # Dosen Tetap & Luar Biasa
├── kurikulum.html          # Kurikulum OBE & KKNI
├── akreditasi.html         # Sertifikat, LED, LKPS
├── kemahasiswaan.html      # Prestasi & Alumni
├── layanan.html            # Links, Job Career
├── media_informasi.html    # Berita & Gallery
├── news_detail.html        # Detail berita
├── documents.html          # Daftar dokumen per kategori
├── search.html             # Hasil pencarian
├── login.html              # Login admin
└── admin/
    └── dashboard.html      # Admin dashboard
```

### 📚 Documentation
```
README.md                   # Project overview & features
PANDUAN_INSTALASI.md        # Installation guide (detailed)
QUICK_START.md              # Quick start (5 minutes)
STRUKTUR_PROJECT.md         # Project structure details
CHANGELOG.md                # Version history
INDEX.md                    # This file
```

### 🗄️ Database
```
database_schema.sql         # SQL schema & sample data
```

### 🪟 Windows Scripts
```
setup_project.bat           # Auto setup script
run_server.bat              # Run development server
```

## 📊 Database Models (16)

| No | Model | Description | Fields |
|----|-------|-------------|--------|
| 1  | Slide | Homepage slider | title, description, image, link, order |
| 2  | Sambutan | Ketua Prodi | ketua_name, photo, content |
| 3  | VisiMisi | Visi & Misi | visi, misi, tujuan |
| 4  | ProspekKeunggulan | Graduate prospects | title, description, icon |
| 5  | Dosen | Faculty | nidn, nama, kategori, photo, email |
| 6  | DocumentCategory | Doc categories | name, slug, description |
| 7  | Document | Documents | title, file, category |
| 8  | News | News articles | title, content, thumbnail |
| 9  | Gallery | Photos & Videos | title, media_type, image/video |
| 10 | Prestasi | Achievements | student_name, achievement, tingkat |
| 11 | Penelitian | Research | title, jenis, peneliti, year |
| 12 | Akreditasi | Accreditation | program, peringkat, certificate |
| 13 | Alumni | Alumni data | nama, nim, tahun_lulus, pekerjaan |
| 14 | JobCareer | Job listings | position, company, deadline |
| 15 | Link | External links | name, url, kategori |
| 16 | PageContent | Static pages | page_name, title, content |

## 🛣️ URL Routes

| URL | View | Template | Feature |
|-----|------|----------|---------|
| / | home | home.html | Homepage |
| /profile/ | profile | profile.html | Visi & Misi |
| /akademik/ | akademik | akademik.html | Dosen |
| /kurikulum/ | kurikulum | kurikulum.html | Kurikulum |
| /akreditasi/ | akreditasi | akreditasi.html | Akreditasi |
| /kemahasiswaan/ | kemahasiswaan | kemahasiswaan.html | Prestasi & Alumni |
| /layanan/ | layanan | layanan.html | Services |
| /media/ | media_informasi | media_informasi.html | News & Gallery |
| /news/<slug>/ | news_detail | news_detail.html | News detail |
| /documents/<slug>/ | documents_by_category | documents.html | Documents |
| /download/<id>/ | download_document | - | Download |
| /search/ | search | search.html | Search |
| /login/ | user_login | login.html | Login |
| /logout/ | user_logout | - | Logout |
| /dashboard/ | admin_dashboard | admin/dashboard.html | Dashboard |
| /admin/ | Django Admin | (built-in) | Admin |

## 🎨 Design System

### Colors
- **Primary (Purple)**: #7e22ce - #581c87
- **Gold**: #f59e0b - #78350f
- **Gradient**: Purple to Gold

### Typography
- **Font**: Poppins (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700

### Icons
- **Font Awesome 6.4.0**
- Usage: `<i class="fas fa-icon-name"></i>`

### Responsive Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1023px
- Desktop: >= 1024px

## 📦 Dependencies

### Backend
- Django 5.0.1
- mysqlclient 2.2.1
- Pillow 10.2.0
- python-decouple 3.8
- django-ckeditor 6.7.0
- django-crispy-forms 2.1
- crispy-tailwind 1.0.3

### Frontend (CDN)
- Tailwind CSS
- Font Awesome 6.4.0
- Google Fonts (Poppins)

## 🚀 Quick Commands

### Setup
```bash
setup_project.bat              # Auto setup (Windows)
python manage.py migrate       # Database migration
python manage.py createsuperuser  # Create admin
```

### Development
```bash
run_server.bat                 # Run server (Windows)
python manage.py runserver     # Run server (Manual)
python manage.py collectstatic # Collect static files
```

### Database
```bash
python manage.py makemigrations  # Create migrations
python manage.py migrate         # Apply migrations
python manage.py shell           # Django shell
```

## 📞 Support

For detailed instructions, refer to:
1. `QUICK_START.md` - Quick 5-minute setup
2. `PANDUAN_INSTALASI.md` - Detailed installation
3. `README.md` - Project overview

---

**Program Studi Sistem Informasi**
**Universitas Nurdin Hamzah**
**© 2025**

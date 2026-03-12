# Website Program Studi Sistem Informasi - Universitas Nurdin Hamzah

Website dinamis dan responsive untuk Program Studi Sistem Informasi menggunakan Django framework dengan tema warna ungu dan emas.

## 🎨 Fitur Utama

### 1. **Homepage**
- Slider dinamis dengan gambar dan deskripsi
- Sambutan Ketua Program Studi
- Berita terkini
- Gallery preview
- Quick stats

### 2. **Profile Prodi**
- Visi, Misi, dan Tujuan
- Prospek dan Keunggulan Lulusan
- Fasilitas

### 3. **Akademik**
- Data Dosen Tetap
- Data Dosen Luar Biasa
- Profil lengkap dosen (foto, email, bidang keahlian, link scholar/scopus/sinta)

### 4. **Kurikulum**
- Kurikulum Berbasis OBE – K22 (upload/download)
- Kurikulum Berbasis KKNI – K17 (upload/download)
- Dokumen kurikulum dinamis

### 5. **Akreditasi**
- Sertifikat Akreditasi
- Laporan Evaluasi Diri (LED) - upload/download
- LKPS - upload/download

### 6. **Kemahasiswaan & Alumni**
- Prestasi Mahasiswa
- Data Ikatan Alumni
- Buku Panduan (Pembimbing Akademik, Seminar, Skripsi) - upload/download
- Tracer Study

### 7. **Layanan**
- Link SIAKAD
- Link V-Class
- Link Open Journal System
- Link Laboratorium
- Pembimbing Akademik (dokumen upload/download)
- Pembimbing Seminar (dokumen upload/download)
- Pembimbing Skripsi (dokumen upload/download)
- Job Career
- Penelitian & Pengabdian

### 8. **Media & Informasi**
- Berita Program Studi (dengan view counter)
- Gallery Foto
- Gallery Video (YouTube/Vimeo embed)

### 9. **Fitur Admin**
- Dashboard admin
- Upload/Download semua jenis dokumen
- Management konten dinamis
- User authentication

## 🛠️ Teknologi yang Digunakan

- **Backend**: Django 5.0.1
- **Frontend**: Tailwind CSS (via CDN)
- **Database**: MySQL (XAMPP)
- **JavaScript**: Vanilla JS
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Poppins)
- **Rich Text Editor**: CKEditor
- **Forms**: Django Crispy Forms with Tailwind

## 📋 Persyaratan Sistem

- Python 3.8+
- MySQL Server (XAMPP)
- pip (Python package manager)

## 🚀 Instalasi

### 1. Clone atau Extract Project

```bash
cd si_unh_website
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Database MySQL (XAMPP)

1. Buka XAMPP Control Panel
2. Start Apache dan MySQL
3. Buka phpMyAdmin (http://localhost/phpmyadmin)
4. Buat database baru dengan nama `si_unh_db`

```sql
CREATE DATABASE si_unh_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Konfigurasi Environment

Buat file `.env` di root project:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database Configuration
DB_NAME=si_unh_db
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

**Generate SECRET_KEY:**

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Buat File __init__.py

```bash
# Di folder si_unh_website/
touch si_unh/__init__.py
touch core/__init__.py
```

### 6. Setup Django Project

```bash
# Jalankan migrasi database
python manage.py makemigrations
python manage.py migrate

# Buat superuser untuk admin
python manage.py createsuperuser
# Ikuti instruksi: masukkan username, email, dan password

# Collect static files
python manage.py collectstatic --noinput
```

### 7. Jalankan Development Server

```bash
python manage.py runserver
```

Website akan berjalan di: **http://127.0.0.1:8000**

Admin panel: **http://127.0.0.1:8000/admin**

## 📁 Struktur Database

### Tabel Utama:

1. **Slide** - Slider homepage
2. **Sambutan** - Sambutan Ketua Prodi
3. **VisiMisi** - Visi & Misi
4. **ProspekKeunggulan** - Prospek Lulusan
5. **Dosen** - Data Dosen
6. **DocumentCategory** - Kategori Dokumen
7. **Document** - Dokumen (upload/download)
8. **News** - Berita
9. **Gallery** - Gallery Foto & Video
10. **Prestasi** - Prestasi Mahasiswa
11. **Penelitian** - Penelitian & Pengabdian
12. **Akreditasi** - Sertifikat Akreditasi
13. **Alumni** - Data Alumni
14. **JobCareer** - Lowongan Kerja
15. **Link** - Link Eksternal
16. **PageContent** - Konten Halaman Statis

## 🎨 Panduan Penggunaan Admin

### Login Admin
1. Akses http://127.0.0.1:8000/admin
2. Login dengan username dan password superuser

### Upload Dokumen
1. Masuk ke Admin Panel
2. Pilih **Document categories** → Tambahkan kategori baru (contoh: "Pembimbing Akademik")
3. Pilih **Documents** → Tambahkan dokumen baru
4. Pilih kategori, isi judul, deskripsi, dan upload file
5. Dokumen akan otomatis tersedia untuk download di website

### Upload Berita
1. Pilih **News** → Add News
2. Isi judul, upload thumbnail, tulis konten
3. Centang "Is published" untuk publikasi
4. Centang "Is featured" untuk berita unggulan

### Upload Slide
1. Pilih **Slides** → Add Slide
2. Upload gambar, isi judul dan deskripsi
3. Atur order (urutan tampil)
4. Aktifkan dengan centang "Is active"

### Manajemen Dosen
1. Pilih **Dosen** → Add Dosen
2. Isi data lengkap (NIDN, nama, email, dll)
3. Upload foto
4. Pilih kategori (Tetap/Luar Biasa)
5. Isi link scholar, scopus, sinta jika ada

## 🎨 Kustomisasi Warna

Website menggunakan tema **Ungu & Emas**. Untuk mengubah warna, edit file `templates/base.html`:

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: { /* Warna Ungu */ },
                gold: { /* Warna Emas */ }
            }
        }
    }
}
```

## 📱 Responsive Design

Website sudah fully responsive untuk:
- Desktop (1920px+)
- Laptop (1024px - 1919px)
- Tablet (768px - 1023px)
- Mobile (320px - 767px)

## 🔐 Security Features

- CSRF Protection
- User Authentication
- File Upload Validation
- SQL Injection Prevention (Django ORM)
- XSS Protection

## 📄 Halaman yang Tersedia

| URL | Halaman |
|-----|---------|
| `/` | Homepage |
| `/profile/` | Profile Prodi |
| `/akademik/` | Akademik (Dosen) |
| `/kurikulum/` | Kurikulum |
| `/akreditasi/` | Akreditasi |
| `/kemahasiswaan/` | Kemahasiswaan & Alumni |
| `/layanan/` | Layanan |
| `/media/` | Media & Informasi |
| `/admin/` | Admin Panel |
| `/login/` | Login |
| `/logout/` | Logout |

## 🔧 Troubleshooting

### Error: No module named 'mysqlclient'
```bash
pip install mysqlclient
```

Jika gagal, install dependencies:
```bash
# Windows
pip install mysqlclient

# Linux/Mac
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient
```

### Error: Can't connect to MySQL
- Pastikan MySQL di XAMPP sudah running
- Cek username/password di .env
- Cek nama database sudah dibuat

### Error: Static files not found
```bash
python manage.py collectstatic --clear --noinput
```

## 📞 Support

Untuk bantuan lebih lanjut, silakan hubungi:
- Email: si@unh.ac.id
- Website: https://si.unh.ac.id

## 📝 License

Copyright © 2025 Program Studi Sistem Informasi - Universitas Nurdin Hamzah

---

**Dibuat dengan ❤️ menggunakan Django & Tailwind CSS**

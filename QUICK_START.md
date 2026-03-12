# 🚀 Quick Start Guide - SI UNH Website

Panduan cepat untuk menjalankan website dalam 5 menit!

## Prasyarat
- ✅ Python 3.8+ terinstall
- ✅ XAMPP terinstall dan running (MySQL)
- ✅ Text editor (VS Code recommended)

## Langkah Cepat

### 1. Extract Project
Extract file `si_unh_website.zip` ke folder pilihan Anda.

### 2. Jalankan Auto Setup
**Windows:**
```bash
# Double-click file:
setup_project.bat
```

**macOS / Linux:**
```bash
# Buka Terminal, arahkan ke folder project:
cd path/to/si_unh_website
chmod +x setup_project.sh
./setup_project.sh
```

### 3. Buat Database di phpMyAdmin
1. Buka: http://localhost/phpmyadmin
2. Klik "New" → Nama: `si_unh_db`
3. Collation: `utf8mb4_unicode_ci`
4. Klik "Create"

### 4. Edit File .env
Buka file `.env` dan edit jika perlu:
```env
SECRET_KEY=generate-with-django
DEBUG=True
DB_NAME=si_unh_db
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

### 5. Generate SECRET_KEY
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copy hasilnya ke file `.env` bagian `SECRET_KEY`

### 6. Migrasi Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Buat Admin User
```bash
python manage.py createsuperuser

# Isi:
# Username: admin
# Email: admin@unh.ac.id
# Password: (password kuat Anda)
```

### 8. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 9. Jalankan Server
**Windows:**
```bash
run_server.bat
```

**macOS / Linux:**
```bash
./run_server.sh
```

Atau manual:
```bash
python manage.py runserver
```

### 10. Akses Website
- **Website**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/Js0312yA11/
  - Username: admin
  - Password: (yang Anda buat tadi)

## ✅ Checklist

- [ ] Python terinstall
- [ ] XAMPP MySQL running
- [ ] Database `si_unh_db` dibuat
- [ ] File `.env` sudah diedit
- [ ] SECRET_KEY sudah di-generate
- [ ] Migrasi database berhasil
- [ ] Superuser sudah dibuat
- [ ] Static files sudah di-collect
- [ ] Server berjalan tanpa error
- [ ] Bisa akses website & admin

## 🎨 Upload Konten Pertama

### 1. Login ke Admin
http://127.0.0.1:8000/admin/

### 2. Upload Slide Homepage
- Klik "Slides" → "Add Slide"
- Upload gambar (1920x1080px recommended)
- Isi title & description
- Set order = 1
- Centang "Is active"
- Save

### 3. Isi Visi & Misi
- Klik "Visi & Misi" → "Add"
- Isi visi, misi, dan tujuan
- Save

### 4. Tambah Dosen
- Klik "Dosen" → "Add Dosen"
- Isi semua data
- Upload foto (800x800px recommended)
- Save

### 5. Tambah Berita
- Klik "News" → "Add News"
- Isi title
- Upload thumbnail
- Tulis content
- Centang "Is published"
- Save

### 6. Upload Dokumen
- Buat kategori dulu di "Document categories"
- Lalu "Documents" → "Add Document"
- Pilih kategori
- Upload file
- Save

## 🛠️ Troubleshooting Cepat

### Error: ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### Error: Database Connection
- Pastikan MySQL XAMPP running
- Cek file `.env` sesuai dengan phpMyAdmin

### Error: Static Files
```bash
python manage.py collectstatic --clear
```

### Port 8000 Busy
```bash
python manage.py runserver 8080
```

## 📞 Butuh Bantuan?

Baca dokumentasi lengkap:
- `README.md` - Overview
- `PANDUAN_INSTALASI.md` - Detail installation
- `STRUKTUR_PROJECT.md` - Project structure

---

**Selamat! Website Anda siap digunakan! 🎉**

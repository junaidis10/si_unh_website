# 🚀 Panduan Instalasi Website SI UNH - Lengkap

## Daftar Isi
1. [Persiapan](#persiapan)
2. [Instalasi Python](#instalasi-python)
3. [Instalasi XAMPP](#instalasi-xampp)
4. [Setup Project](#setup-project)
5. [Konfigurasi Database](#konfigurasi-database)
6. [Menjalankan Website](#menjalankan-website)
7. [Upload Konten](#upload-konten)
8. [Troubleshooting](#troubleshooting)

---

## 1. Persiapan

### Tools yang Diperlukan:
- ✅ Python 3.8 atau lebih baru
- ✅ XAMPP (untuk MySQL Server)
- ✅ Text Editor (VS Code, Sublime, dll)
- ✅ Browser (Chrome, Firefox, Edge)

---

## 2. Instalasi Python

### Windows:

1. **Download Python**
   - Kunjungi: https://www.python.org/downloads/
   - Download Python versi terbaru (3.8+)

2. **Install Python**
   - Jalankan installer
   - ⚠️ **PENTING**: Centang "Add Python to PATH"
   - Klik "Install Now"

3. **Verifikasi Instalasi**
   ```bash
   # Buka Command Prompt (CMD)
   python --version
   # Output: Python 3.x.x
   
   pip --version
   # Output: pip 23.x.x
   ```

---

## 3. Instalasi XAMPP

### Download & Install:

1. **Download XAMPP**
   - Kunjungi: https://www.apachefriends.org/
   - Download XAMPP for Windows

2. **Install XAMPP**
   - Jalankan installer
   - Install di `C:\xampp`
   - Centang Apache dan MySQL

3. **Jalankan XAMPP**
   - Buka XAMPP Control Panel
   - Klik "Start" pada Apache
   - Klik "Start" pada MySQL
   - Pastikan statusnya hijau (Running)

4. **Verifikasi MySQL**
   - Buka browser
   - Akses: http://localhost/phpmyadmin
   - Jika muncul interface phpMyAdmin = berhasil!

---

## 4. Setup Project

### Langkah 1: Extract Project

```bash
# Extract file si_unh_website.zip ke folder pilihan
# Misal: C:\Projects\si_unh_website
```

### Langkah 2: Buka Command Prompt di Folder Project

```bash
# Cara 1: Melalui File Explorer
# - Buka folder project
# - Shift + Klik kanan di area kosong
# - Pilih "Open PowerShell window here" atau "Open command window here"

# Cara 2: Manual
cd C:\Projects\si_unh_website
```

### Langkah 3: Buat Virtual Environment (Opsional tapi Direkomendasikan)

```bash
# Buat virtual environment
python -m venv venv

# Aktivasi virtual environment
# Windows CMD:
venv\Scripts\activate

# Windows PowerShell:
venv\Scripts\Activate.ps1

# Setelah aktif, akan ada (venv) di awal command prompt
```

### Langkah 4: Install Dependencies

```bash
# Install semua package yang diperlukan
pip install -r requirements.txt

# Tunggu sampai selesai (bisa 2-5 menit)
```

**Catatan**: Jika ada error saat install `mysqlclient`:

```bash
# Download wheel file dari:
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

# Install manual:
pip install mysqlclient‑1.4.6‑cp39‑cp39‑win_amd64.whl
# (sesuaikan dengan versi Python Anda)
```

---

## 5. Konfigurasi Database

### Langkah 1: Buat Database

1. Buka phpMyAdmin: http://localhost/phpmyadmin
2. Klik "New" di sidebar kiri
3. Nama database: `si_unh_db`
4. Collation: `utf8mb4_unicode_ci`
5. Klik "Create"

### Langkah 2: Konfigurasi .env

```bash
# Copy file .env.example menjadi .env
copy .env.example .env
```

Edit file `.env`:

```env
# Generate SECRET_KEY dulu
# Jalankan command:
# python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

SECRET_KEY=hasil-generate-secret-key-di-sini
DEBUG=True

DB_NAME=si_unh_db
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

### Langkah 3: Buat Struktur Folder yang Diperlukan

```bash
# Buat folder __init__.py
type nul > si_unh\__init__.py
type nul > core\__init__.py

# Buat folder media
mkdir media
mkdir static
```

### Langkah 4: Migrasi Database

```bash
# Generate file migrasi
python manage.py makemigrations

# Apply migrasi ke database
python manage.py migrate

# Jika sukses, akan ada pesan:
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, core, sessions
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   ... (dan seterusnya)
```

### Langkah 5: Buat Superuser (Admin)

```bash
python manage.py createsuperuser

# Isi data yang diminta:
# Username: admin
# Email address: admin@unh.ac.id
# Password: (masukkan password yang kuat)
# Password (again): (ketik ulang password)
```

### Langkah 6: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

---

## 6. Menjalankan Website

### Start Development Server:

```bash
python manage.py runserver

# Output:
# Django version 5.0.1, using settings 'si_unh.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.
```

### Akses Website:

1. **Website Public**: http://127.0.0.1:8000/
2. **Admin Panel**: http://127.0.0.1:8000/admin/
   - Username: admin
   - Password: (yang Anda buat tadi)

---

## 7. Upload Konten

### Cara Upload Dokumen:

1. Login ke Admin Panel: http://127.0.0.1:8000/admin/
2. **Upload Slide Homepage:**
   - Klik "Slides" → "Add Slide"
   - Upload gambar, isi judul & deskripsi
   - Centang "Is active"
   - Klik "Save"

3. **Tambah Sambutan Ketua Prodi:**
   - Klik "Sambutan" → "Add Sambutan"
   - Isi nama ketua, jabatan
   - Upload foto
   - Isi content (sambutan)
   - Centang "Is active"
   - Klik "Save"

4. **Upload Dokumen:**
   - **Buat Kategori Dulu:**
     - Klik "Document categories" → "Add Document Category"
     - Contoh: "Pembimbing Akademik"
     - Slug auto-generate
     - Klik "Save"
   
   - **Upload Dokumen:**
     - Klik "Documents" → "Add Document"
     - Pilih kategori
     - Isi title & description
     - Upload file
     - Centang "Is active"
     - Klik "Save"

5. **Tambah Dosen:**
   - Klik "Dosen" → "Add Dosen"
   - Isi semua data (NIDN, nama, email, dll)
   - Upload foto dosen
   - Pilih kategori (Tetap/Luar Biasa)
   - Centang "Is active"
   - Klik "Save"

6. **Tambah Berita:**
   - Klik "News" → "Add News"
   - Isi title
   - Upload thumbnail
   - Tulis content
   - Centang "Is published"
   - Klik "Save"

### Tips Upload:
- **Format Gambar**: JPG, PNG (max 5MB)
- **Format Dokumen**: PDF, DOCX, XLSX (max 10MB)
- **Ukuran Slide**: 1920x1080px (landscape)
- **Ukuran Foto Dosen**: 800x800px (square)

---

## 8. Troubleshooting

### Problem 1: Error "No module named 'MySQLdb'"

**Solusi:**
```bash
pip install mysqlclient --upgrade
```

### Problem 2: Database Connection Error

**Solusi:**
1. Pastikan MySQL di XAMPP sudah running
2. Cek file `.env`:
   - DB_NAME harus sama dengan database di phpMyAdmin
   - DB_USER biasanya `root`
   - DB_PASSWORD kosong (default XAMPP)
3. Test koneksi:
   ```bash
   python manage.py shell
   >>> from django.db import connection
   >>> connection.ensure_connection()
   >>> exit()
   ```

### Problem 3: Static Files Not Found

**Solusi:**
```bash
python manage.py collectstatic --clear --noinput
```

### Problem 4: Port 8000 Already in Use

**Solusi:**
```bash
# Gunakan port lain
python manage.py runserver 8080
# Akses: http://127.0.0.1:8080/
```

### Problem 5: Error saat Upload File

**Solusi:**
1. Pastikan folder `media` sudah dibuat
2. Cek permission folder
3. Restart development server

### Problem 6: Admin Interface Berantakan (No CSS)

**Solusi:**
```bash
python manage.py collectstatic --noinput
# Reload browser dengan Ctrl+F5
```

---

## 🎉 Selesai!

Sekarang website Anda sudah berjalan!

### Checklist Final:
- ✅ Website bisa diakses di http://127.0.0.1:8000/
- ✅ Admin panel bisa diakses di http://127.0.0.1:8000/admin/
- ✅ Bisa login ke admin
- ✅ Bisa upload dokumen
- ✅ Bisa menambah berita
- ✅ Bisa upload slide

### Next Steps:
1. Lengkapi Visi & Misi
2. Upload data semua dosen
3. Upload dokumen-dokumen
4. Tambahkan berita
5. Upload gallery

---

## 📞 Butuh Bantuan?

Jika mengalami masalah:
1. Cek file log di console
2. Lihat error message dengan teliti
3. Pastikan semua langkah sudah diikuti
4. Restart XAMPP & Development Server

---

**Good luck! 🚀**

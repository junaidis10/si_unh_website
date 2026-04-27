# SI UNH Website - Program Studi Sistem Informasi

Website resmi Program Studi Sistem Informasi Universitas Nurdin Hamzah (UNH). Platform ini dirancang untuk menyediakan layanan akademik, informasi publik, dan manajemen publikasi bagi dosen dan mahasiswa.

## Fitur Utama

- **Layanan Akademik**: Aktivasi V-Class, informasi kurikulum, dan download dokumen.
- **Riset & Publikasi**: Showcase buku karya dosen dan publikasi jurnal (Sinta, Scopus, Prosiding).
- **Media & Informasi**: Berita terkini dan galeri dokumentasi kegiatan prodi.
- **Survei Digital**: Pengumpulan data pemahaman VMTS, kepuasan pengguna lulusan, dan evaluasi kurikulum.
- **Dashboard Admin**: Manajemen konten yang mudah bagi staf program studi.

## Teknologi

- **Backend**: Python 3.13, Django 5.0
- **Frontend**: Tailwind CSS, Vanilla JS, Font Awesome
- **Database**: MySQL (XAMPP/MariaDB)
- **Editor**: CKEditor (Rich Text Editing)

## Instalasi

1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/si_unh_website.git
   cd si_unh_website
   ```

2. **Setup Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Konfigurasi Environment**:
   Salin file `.env.example` menjadi `.env` dan sesuaikan dengan database lokal Anda.
   ```bash
   cp .env.example .env
   ```

5. **Database Migration**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**:
   ```bash
   python manage.py runserver
   ```

## Konfigurasi Database (MySQL)

Pastikan XAMPP/MySQL berjalan dan buatlah database dengan nama `si_unh_db` (atau sesuai konfigurasi `.env`).

## Struktur Proyek

- `core/`: Aplikasi utama (models, views, logic).
- `templates/`: File HTML dengan Tailwind CSS.
- `static/`: Aset statis (CSS, JS).
- `media/`: File unggahan (Foto Dosen, Thumbnail Berita, Dokumen).

---
© 2025 Program Studi Sistem Informasi - Universitas Nurdin Hamzah

# 🌐 Panduan Deployment SI UNH Website

Panduan ini menjelaskan langkah-langkah untuk mendeploy website SI UNH ke server produksi (VPS Ubuntu) agar dapat diakses melalui domain **si.unh.ac.id**.

## 🏗️ Persiapan Server (Ubuntu 22.04 LTS)

### 1. Update System & Install Dependencies
```bash
sudo apt update
sudo apt install python3-pip python3-dev default-libmysqlclient-dev build-essential libssl-dev libffi-dev python3-setuptools
sudo apt install nginx curl
```

### 2. Install & Konfigurasi MySQL (Jika belum ada)
```bash
sudo apt install mysql-server
sudo mysql_secure_installation
```
Buat database dan user untuk Django:
```sql
CREATE DATABASE si_unh_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'si_admin'@'localhost' IDENTIFIED BY 'PasswordKuatAnda';
GRANT ALL PRIVILEGES ON si_unh_db.* TO 'si_admin'@'localhost';
FLUSH PRIVILEGES;
```

---

## 🚀 Setup Project di Server

### 1. Clone Project
```bash
cd /var/www
sudo git clone https://github.com/username/si_unh_website.git
sudo chown -R $USER:$USER si_unh_website
cd si_unh_website
```

### 2. Setup Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn setproctitle
```

### 3. Konfigurasi Environment (`.env`)
Buat file `.env` di folder project:
```env
DEBUG=False
SECRET_KEY=isi-dengan-secret-key-yang-aman
ALLOWED_HOSTS=si.unh.ac.id,www.si.unh.ac.id,127.0.0.1

DB_NAME=si_unh_db
DB_USER=si_admin
DB_PASSWORD=PasswordKuatAnda
DB_HOST=localhost
DB_PORT=3306
```

### 4. Persiapan Django
```bash
python manage.py collectstatic
python manage.py migrate
```

---

## ⚙️ Konfigurasi Layanan

### 1. Setup Gunicorn (Systemd Service)
Buat file service: `sudo nano /etc/systemd/system/si_unh.service`
```ini
[Unit]
Description=gunicorn daemon for SI UNH Website
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/si_unh_website
ExecStart=/var/www/si_unh_website/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/si_unh.sock \
          si_unh.wsgi:application

[Install]
WantedBy=multi-user.target
```
Jalankan service:
```bash
sudo systemctl start si_unh
sudo systemctl enable si_unh
```

### 2. Setup Nginx (Reverse Proxy)
Buat konfigurasi site: `sudo nano /etc/nginx/sites-available/si_unh`
```nginx
server {
    listen 80;
    server_name si.unh.ac.id www.si.unh.ac.id;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/si_unh_website;
    }

    location /media/ {
        root /var/www/si_unh_website;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/si_unh.sock;
    }
}
```
Aktifkan konfigurasi:
```bash
sudo ln -s /etc/nginx/sites-available/si_unh /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

---

## 🔒 Keamanan (SSL HTTPS)

Gunakan Let's Encrypt untuk mendapatkan sertifikat SSL gratis:
```bash
sudo apt install python3-certbot-nginx
sudo certbot --nginx -d si.unh.ac.id -d www.si.unh.ac.id
```

---

## 📝 Catatan Penting
- **DEBUG**: Pastikan selalu `DEBUG=False` di server produksi.
- **Permission**: Jika gambar tidak muncul, pastikan folder `media` dan `static` memiliki permission yang benar (biasanya `chown -R www-data:www-data media`).
- **Database Backup**: Lakukan backup database secara rutin menggunakan `mysqldump`.

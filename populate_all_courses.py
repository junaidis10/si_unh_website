import os
import django
import pandas as pd

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'si_unh.settings')
django.setup()

from core.models import MataKuliah

def populate_courses():
    data = []
    
    # Semester 1
    data.append((1, 'SIKK1201', 'Pengantar Manajemen', 2, 'Wajib'))
    data.append((1, 'FKPN1201', 'Aljabar Vektor dan Matriks', 2, 'Wajib'))
    data.append((1, 'SIKK1302', 'Sistem Dan Teknologi Informasi', 3, 'Wajib'))
    data.append((1, 'SIKK1403', 'Pemrogramman Dasar (P)', 4, 'Wajib'))
    data.append((1, 'FKKK1402', 'Algorithma dan Pemrograman (P)', 4, 'Wajib'))
    data.append((1, 'FKKK1403', 'Sistem Operasi dan Arsitektur Komputer (P)', 3, 'Wajib'))
    
    # Semester 2
    data.append((2, 'SIPN2202', 'Pengantar Akuntansi', 2, 'Wajib'))
    data.append((2, 'PK2201', 'Pendidikan Agama', 2, 'Wajib'))
    data.append((2, 'NHPN2303', 'Statistika dan Penerapan', 3, 'Wajib'))
    data.append((2, 'SIPN2204', 'Bahasa Inggris I', 3, 'Wajib'))
    data.append((2, 'PK2204', 'Bahasa Indonesia', 2, 'Wajib'))
    data.append((2, 'SIPN2205', 'Matematika Komputasi', 2, 'Wajib'))
    data.append((2, 'SIKK2304', 'Algoritma dan Pemrograman (P II)', 3, 'Wajib'))
    data.append((2, 'NHKK2302', 'Aplikasi Perkantoran (P)', 3, 'Wajib'))
    
    # Semester 3
    data.append((3, 'SIKK3305', 'Sistem Informasi Manajemen', 3, 'Wajib'))
    data.append((3, 'SIKK3306', 'Manajemen Investasi Teknologi Informasi', 3, 'Wajib'))
    data.append((3, 'SIKK3207', 'Manajemen Proses Bisnis', 2, 'Wajib'))
    data.append((3, 'SIKK3308', 'Konsep Sistem Informasi', 3, 'Wajib'))
    data.append((3, 'PK3202', 'Pendidikan Pancasila', 2, 'Wajib'))
    data.append((3, 'FKKB3304', 'Manajemen & Sistem Basis Data', 3, 'Wajib'))
    data.append((3, 'SIKB3301', 'Pemrograman Berbasis Platform (P)', 4, 'Wajib'))
    data.append((3, 'SIPN3306', 'Bahasa Inggris II', 2, 'Wajib'))
    
    # Semester 4
    data.append((4, 'SIKB3302', 'Teknologi Basis Data', 3, 'Wajib'))
    data.append((4, 'SIKK4309', 'Analisis dan Perancangan Sistem Informasi', 3, 'Wajib'))
    data.append((4, 'FKKK4305', 'Komunikasi Data dan Jaringan Komputer (P)', 3, 'Wajib'))
    data.append((4, 'SIKK4311', 'Tata Kelola Teknologi Informasi', 3, 'Wajib'))
    data.append((4, 'SIKK4312', 'Manajemen Sains', 3, 'Wajib'))
    data.append((4, 'PK4203', 'Pendidikan Kewarganegaraan', 2, 'Wajib'))
    data.append((4, 'SIKK4213', 'Arsitektur SI/IT Perusahaan', 2, 'Wajib'))
    data.append((4, 'SIKB4303', 'Matakuliah Pilihan 1', 3, 'Wajib'))
    data.append((4, 'SIKM401', 'Lintas Prodi / MBKM', 0, 'Wajib'))
    
    # Semester 5
    data.append((5, 'SIKK5314', 'Analisis dan Manajemen Jaringan (P)', 3, 'Wajib'))
    data.append((5, 'SIKB5304', 'Audit Sistem informasi', 3, 'Wajib'))
    data.append((5, 'SIKK5315', 'Manajemen Proyek SI', 3, 'Wajib'))
    data.append((5, 'SIPN5307', 'Testing dan Implementasi Sistem Informasi', 3, 'Wajib'))
    data.append((5, 'NHKK5203', 'Technopreneur', 2, 'Wajib'))
    data.append((5, 'FKKK5406', 'Pemrograman berbasis Web (P)', 4, 'Wajib'))
    data.append((5, 'SIKB5304', 'Matakuliah Pilihan 2', 3, 'Wajib'))
    data.append((5, 'SIKM502', 'Lintas Prodi / MBKM', 0, 'Wajib'))
    
    # Semester 6
    data.append((6, 'FKKK6307', 'Metode Penelitian', 3, 'Wajib'))
    data.append((6, 'SIKK6316', 'Sistem Multimedia', 3, 'Wajib'))
    data.append((6, 'FKKK6208', 'Komputer dan Masyarakat', 2, 'Wajib'))
    data.append((6, 'SIKB6306', 'Sistem Pendukung Keputusan Berbasis Model', 3, 'Wajib'))
    data.append((6, 'SIKB6407', 'Rekayasa Web', 4, 'Wajib'))
    data.append((6, 'SIKB6307', 'Matakuliah Pilihan 3', 3, 'Wajib'))
    data.append((6, 'SIKB6409', 'Matakuliah Pilihan 4', 4, 'Wajib'))
    data.append((6, 'SIKM603', 'MBKM / Magang Industri Dll', 0, 'Wajib'))
    
    # Semester 7
    data.append((7, 'FKPB7209', 'Etika Profesi', 2, 'Wajib'))
    data.append((7, 'NHPB7404', 'Kerja Praktek', 4, 'Wajib'))
    data.append((7, 'SIKK7217', 'Interpersonal Skill', 2, 'Wajib'))
    data.append((7, 'SIKB7210', 'Interaksi Manusia dan Komputer', 2, 'Wajib'))
    data.append((7, 'SIKB7311', 'Matakuliah Pilihan 5', 3, 'Wajib'))
    data.append((7, 'SIKB7314', 'Matakuliah Pilihan 6', 3, 'Wajib'))
    data.append((7, 'SIKM704', 'MBKM / Magang Industri Dll', 0, 'Wajib'))
    
    # Semester 8
    data.append((8, 'SIKB8613', 'Skripsi', 6, 'Wajib'))
    
    # Matakuliah Pilihan (Semester 0)
    pilihan_list = [
        ('SIKB4301', 'Sistem Informasi Akuntansi', 3, 'MP1'),
        ('SIKB4302', 'Sistem Informasi Perbankan', 3, 'MP1'),
        ('SIKB4303', 'Konsep Data Mining', 3, 'MP1'),
        ('SIKB5304', 'Grafika Komputer & Pengolahan Citra', 3, 'MP2'),
        ('SIKB5305', 'Bisnis Digital', 3, 'MP2'),
        ('SIKB5306', 'Pengantar Model & Simulasi', 3, 'MP2'),
        ('SIKB6307', 'Rekayasa Perangkat Lunak', 3, 'MP3'),
        ('SIKB6308', 'Sistem Terdistribusi', 3, 'MP3'),
        ('SIKB6409', 'Pemrograman Berorientasi Objek', 4, 'MP4'),
        ('SIKB6410', 'Pemrograman Mobile', 4, 'MP4'),
        ('SIKB7311', 'Keamanan Sistem Informasi (P)', 3, 'MP5'),
        ('SIKB7312', 'Pemasaran Digital', 3, 'MP5'),
        ('SIKB7313', 'Pengantar Digital Forensic IT', 3, 'MP6'),
        ('SIKB7314', 'Sistem Cerdas', 3, 'MP6'),
    ]
    
    for kode, nama, sks, note in pilihan_list:
        data.append((0, kode, nama, sks, f'Pilihan ({note})'))

    # Clear all data to ensure complete correctness
    MataKuliah.objects.all().delete()
    
    # Insert new data
    for i, (smtr, kode, nama, sks, kat) in enumerate(data):
        MataKuliah.objects.create(
            kode=kode,
            nama=nama,
            sks=sks,
            semester=smtr,
            kategori=kat,
            order=i,
            is_active=True
        )
    
    print(f"Successfully populated {len(data)} courses.")

if __name__ == '__main__':
    populate_courses()

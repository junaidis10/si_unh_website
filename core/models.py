from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Slide(models.Model):
    """Model untuk slideshow homepage"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='slides/')
    link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class Sambutan(models.Model):
    """Sambutan Ketua Program Studi"""
    title = models.CharField(max_length=200, default='Sambutan Ketua Program Studi')
    ketua_name = models.CharField(max_length=100)
    ketua_photo = models.ImageField(upload_to='sambutan/')
    jabatan = models.CharField(max_length=100, default='Ketua Program Studi Sistem Informasi')
    content = RichTextField()
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Sambutan'
    
    def __str__(self):
        return f'Sambutan - {self.ketua_name}'


class VisiMisi(models.Model):
    """Visi dan Misi Program Studi"""
    visi = RichTextField()
    misi = RichTextField()
    tujuan = RichTextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Visi & Misi'
    
    def __str__(self):
        return 'Visi & Misi Program Studi'


class ProspekKeunggulan(models.Model):
    """Prospek dan Keunggulan Lulusan"""
    title = models.CharField(max_length=200)
    description = RichTextField()
    icon = models.CharField(max_length=50, blank=True, help_text='Font Awesome icon class')
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Prospek & Keunggulan'
    
    def __str__(self):
        return self.title


class Dosen(models.Model):
    """Data Dosen"""
    KATEGORI_CHOICES = [
        ('tetap', 'Dosen Tetap'),
        ('dtpr', 'Dosen Tetap Penghitung Rasio'),
        ('luar_biasa', 'Dosen Luar Biasa'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='dosen_profile')
    nidn = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    kategori = models.CharField(max_length=28, choices=KATEGORI_CHOICES, default='tetap')
    photo = models.ImageField(upload_to='dosen/', blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    pendidikan = models.CharField(max_length=200)
    bidang_keahlian = models.CharField(max_length=200)
    scholar_link = models.URLField(blank=True)
    scopus_link = models.URLField(blank=True)
    sinta_link = models.URLField(blank=True)
    bio = RichTextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Dosen'
        ordering = ['nama']
    
    def __str__(self):
        return f'{self.nama} - {self.nidn}'

    def save(self, *args, **kwargs):
        # Auto-create User if not exists
        if not self.user and self.nidn:
            from django.contrib.auth.models import User, Group
            username = self.nidn
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': self.nama[:30],
                    'email': self.email,
                    'is_staff': True  # Agar bisa login ke Admin
                }
            )
            if created:
                user.set_password(self.nidn) # Default password: NIDN
                user.save()
            self.user = user
            
            # Tambahkan ke grup Dosen
            group, _ = Group.objects.get_or_create(name='Dosen')
            user.groups.add(group)
            
        super().save(*args, **kwargs)


class DocumentCategory(models.Model):
    """Kategori Dokumen"""
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Kategori Dokumen'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Document(models.Model):
    """Dokumen yang bisa diupload dan download"""
    category = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='documents/%Y/%m/')
    file_size = models.CharField(max_length=50, blank=True)
    thumbnail = models.ImageField(upload_to='document_thumbnails/', blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    download_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f'{self.title} - {self.category.name}'
    
    def increment_download(self):
        self.download_count += 1
        self.save()


class News(models.Model):
    """Berita Program Studi"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    thumbnail = models.ImageField(upload_to='news/')
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = 'News'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def increment_views(self):
        self.views += 1
        self.save()


class Gallery(models.Model):
    """Gallery Foto dan Video"""
    MEDIA_TYPE_CHOICES = [
        ('image', 'Foto'),
        ('video', 'Video'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='image')
    image = models.ImageField(upload_to='gallery/', blank=True)
    video_url = models.URLField(blank=True, help_text='YouTube or Vimeo URL')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-uploaded_at']
        verbose_name_plural = 'Gallery'
    
    def __str__(self):
        return self.title

    @property
    def embed_url(self):
        if self.video_url:
            import re
            # Regex for YouTube ID extraction
            yt_regex = r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})'
            match = re.search(yt_regex, self.video_url)
            if match:
                video_id = match.group(1)
                return f"https://www.youtube.com/embed/{video_id}"
            
            # Fallback for standard replacement if regex fails
            if "watch?v=" in self.video_url:
                return self.video_url.replace("watch?v=", "embed/")
        return self.video_url


class Prestasi(models.Model):
    """Prestasi Mahasiswa"""
    TINGKAT_CHOICES = [
        ('internasional', 'Internasional'),
        ('nasional', 'Nasional'),
        ('regional', 'Regional'),
        ('lokal', 'Lokal'),
    ]
    
    student_name = models.CharField(max_length=100)
    achievement = models.CharField(max_length=200)
    tingkat = models.CharField(max_length=20, choices=TINGKAT_CHOICES)
    year = models.IntegerField()
    description = RichTextField(blank=True)
    certificate = models.FileField(upload_to='prestasi/', blank=True)
    photo = models.ImageField(upload_to='prestasi/photos/', blank=True)
    date_achieved = models.DateField()
    
    class Meta:
        ordering = ['-date_achieved']
        verbose_name_plural = 'Prestasi Mahasiswa'
    
    def __str__(self):
        return f'{self.student_name} - {self.achievement}'


class Penelitian(models.Model):
    """Penelitian, PKM, dan Publikasi"""
    JENIS_CHOICES = [
        ('penelitian', 'Penelitian (Riset)'),
        ('pkm', 'PKM (Pengabdian Masyarakat)'),
        ('publikasi', 'Publikasi Artikel Jurnal'),
        ('buku', 'Buku (Referensi/Monograf)'),
    ]
    TIPE_PENELITI_CHOICES = [
        ('dosen', 'Dosen'),
        ('mahasiswa', 'Mahasiswa'),
        ('participant', 'Participant'),
    ]
    
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='penelitian_owned', verbose_name="Pemilik Data")
    title = models.CharField(max_length=300, verbose_name="Judul Karya")
    jenis = models.CharField(max_length=20, choices=JENIS_CHOICES, verbose_name="Jenis Karya")
    tipe_peneliti = models.CharField(max_length=20, choices=TIPE_PENELITI_CHOICES, default='dosen', verbose_name="Kategori Peneliti")
    peneliti = models.CharField(max_length=200, help_text='Nama peneliti (pisahkan dengan koma)', verbose_name="Nama Peneliti / Penulis")
    year = models.IntegerField(verbose_name="Tahun")
    abstrak = RichTextField(verbose_name="Abstrak / Deskripsi")
    file = models.FileField(upload_to='penelitian/', blank=True, verbose_name="File Dokumen")
    link = models.URLField(max_length=1000, blank=True, verbose_name="Link Publikasi")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-year', '-created_at']
        verbose_name_plural = 'Penelitian & Pengabdian'
    
    def __str__(self):
        return f'{self.title} ({self.year})'


class Akreditasi(models.Model):
    """Sertifikat Akreditasi"""
    program = models.CharField(max_length=100, default='Program Studi Sistem Informasi')
    peringkat = models.CharField(max_length=20)
    nomor_sk = models.CharField(max_length=100)
    tanggal_sk = models.DateField()
    masa_berlaku = models.DateField()
    lembaga = models.CharField(max_length=100, default='BAN-PT')
    certificate_file = models.FileField(upload_to='akreditasi/')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-tanggal_sk']
        verbose_name_plural = 'Akreditasi'
    
    def __str__(self):
        return f'{self.program} - {self.peringkat}'


class Alumni(models.Model):
    """Data Ikatan Alumni"""
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=20)
    tahun_lulus = models.IntegerField()
    pekerjaan = models.CharField(max_length=200, blank=True)
    perusahaan = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='alumni/', blank=True)
    testimoni = models.TextField(blank=True)
    linkedin = models.URLField(blank=True)
    
    class Meta:
        ordering = ['-tahun_lulus']
        verbose_name_plural = 'Alumni'
    
    def __str__(self):
        return f'{self.nama} ({self.tahun_lulus})'


class JobCareer(models.Model):
    """Lowongan Pekerjaan"""
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50, default='Full Time')
    description = RichTextField()
    requirements = RichTextField()
    salary_range = models.CharField(max_length=100, blank=True)
    application_deadline = models.DateField()
    contact_email = models.EmailField()
    link = models.URLField(blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-posted_date']
        verbose_name_plural = 'Job Career'
    
    def __str__(self):
        return f'{self.position} - {self.company}'


class Link(models.Model):
    """Link Eksternal"""
    KATEGORI_CHOICES = [
        ('siakad', 'SIAKAD'),
        ('vclass', 'V-Class'),
        ('ojs', 'Open Journal System'),
        ('laboratorium', 'Laboratorium'),
        ('lainnya', 'Lainnya'),
    ]
    
    name = models.CharField(max_length=100)
    url = models.URLField()
    kategori = models.CharField(max_length=20, choices=KATEGORI_CHOICES)
    icon = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name


class PageContent(models.Model):
    """Konten Halaman Statis"""
    page_name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Konten Halaman'
    
    def __str__(self):
        return self.page_name
class MataKuliah(models.Model):
    """Model untuk daftar mata kuliah per semester"""
    SEMESTER_CHOICES = [
        (1, 'Semester 1'),
        (2, 'Semester 2'),
        (3, 'Semester 3'),
        (4, 'Semester 4'),
        (5, 'Semester 5'),
        (6, 'Semester 6'),
        (7, 'Semester 7'),
        (8, 'Semester 8'),
        (0, 'Mata Kuliah Pilihan'),
    ]
    
    kode = models.CharField(max_length=20)
    nama = models.CharField(max_length=200)
    sks = models.IntegerField()
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    kategori = models.CharField(max_length=50, blank=True)  # wajib, pilihan, dll
    deskripsi = models.TextField(blank=True)
    
    # RPS Integration fields
    rps_document = models.ForeignKey('Document', on_delete=models.SET_NULL, null=True, blank=True, related_name='mata_kuliah', help_text="Pilih dokumen RPS yang sesuai")
    dosen_pengampu_legacy = models.TextField(blank=True, help_text="Data lama dosen pengampu (text)")
    dosen_pengampu = models.ManyToManyField('Dosen', blank=True, related_name='mata_kuliah_diampu', help_text="Pilih dosen pengampu dari data dosen yang ada")
    materi_perkuliahan = models.TextField(blank=True, help_text="Ringkasan materi perkuliahan")

    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['semester', 'order']
        verbose_name_plural = 'Mata Kuliah'
    
    def __str__(self):
        return f'{self.kode} - {self.nama}'

class BukuPanduan(Document):
    """Proxy model for Buku Panduan category"""
    class Meta:
        proxy = True
        verbose_name = 'Buku Panduan'
        verbose_name_plural = 'Buku Panduan'

class SurveyResponse(models.Model):
    # Identitas Responden
    STATUS_CHOICES = [
        ('pimpinan', 'Pimpinan/Prodi'), ('karyawan', 'Karyawan'),
        ('stakeholder', 'Stakeholder'), ('dosen', 'Dosen/Tenaga Pengajar'),
        ('alumni', 'Alumni'), ('mahasiswa', 'Mahasiswa/Mahasiswi'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    lama_bergabung = models.CharField(max_length=50)

    # Sosialisasi
    pengetahuan_visi = models.CharField(max_length=50)
    sumber_informasi = models.JSONField()  # Untuk menyimpan pilihan ganda (checkbox)
    frekuensi_sosialisasi = models.CharField(max_length=50)

    # Pemahaman & Analisis
    tingkat_paham = models.CharField(max_length=50)
    aspek_tercermin = models.CharField(max_length=50)
    bidang_tercermin = models.JSONField() 
    dukungan_atmosfer = models.CharField(max_length=50)
    perlu_perbaikan = models.CharField(max_length=50)
    saran_kritik = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Survey Responses'
        ordering = ['-created_at']

    def __str__(self):
        return f'Survey from {self.get_status_display()} at {self.created_at}'

class SurveyKepuasanLulusan(models.Model):
    SKALA_CHOICES = [
        ('Sangat Baik', 'Sangat Baik'),
        ('Baik', 'Baik'),
        ('Cukup', 'Cukup'),
        ('Kurang', 'Kurang'),
    ]

    WT_CHOICES = [
        ('WT < 3', 'WT < 3 bulan'),
        ('6 <= WT <= 18', '6 ≤ WT ≤ 18 bulan'),
        ('WT < 18', 'WT < 18 bulan'),
        ('24 <= WT <= 36', '24 ≤ WT ≤ 36 bulan'),
    ]

    # Identitas Responden
    email = models.EmailField()
    nama_responden = models.CharField(max_length=255)
    nama_instansi = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=100)

    # Penilaian Kompetensi
    integritas = models.CharField(max_length=20, choices=SKALA_CHOICES)
    keahlian_bidang = models.CharField(max_length=20, choices=SKALA_CHOICES)
    bahasa_inggris = models.CharField(max_length=20, choices=SKALA_CHOICES)
    penggunaan_it = models.CharField(max_length=20, choices=SKALA_CHOICES)
    komunikasi = models.CharField(max_length=20, choices=SKALA_CHOICES)
    kerjasama_tim = models.CharField(max_length=20, choices=SKALA_CHOICES)
    pengembangan_diri = models.CharField(max_length=20, choices=SKALA_CHOICES)

    # Indikator Kerja
    waktu_tunggu = models.CharField(max_length=50, choices=WT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Survey Kepuasan Lulusan'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nama_instansi} - {self.nama_responden}"

class SurveyKurikulum(models.Model):
    KATEGORI_CHOICES = [
        ('alumni', 'Alumni'),
        ('pakar', 'Dewan Pakar'),
        ('pengguna', 'Pengguna Lulusan'),
        ('stakeholder', 'Stakeholder'),
    ]
    
    # Identitas Responden
    nama_responden = models.CharField(max_length=255)
    kategori_responden = models.CharField(max_length=20, choices=KATEGORI_CHOICES)
    instansi = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    
    # Data Instrumen (JSON)
    responses_data = models.JSONField(default=dict, help_text="Data spesifik kuesioner berdasarkan instrumen kategori")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Survey Kurikulum'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.get_kategori_responden_display()} - {self.nama_responden}'

class JadwalKuliah(models.Model):
    HARI_CHOICES = [
        ('Senin', 'Senin'),
        ('Selasa', 'Selasa'),
        ('Rabu', 'Rabu'),
        ('Kamis', 'Kamis'),
        ('Jumat', 'Jumat'),
        ('Sabtu', 'Sabtu'),
    ]
    
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE, related_name='jadwal', help_text="Pilih Mata Kuliah")
    hari = models.CharField(max_length=20, choices=HARI_CHOICES)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    ruangan = models.CharField(max_length=50)
    kelas = models.CharField(max_length=50, blank=True, help_text="Contoh: SI-1, Reguler A")
    dosen_pengampu = models.ManyToManyField(Dosen, blank=True, related_name='jadwal_diampu')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Jadwal Kuliah'
        ordering = ['hari', 'jam_mulai']

    def __str__(self):
        return f'{self.mata_kuliah.nama} ({self.kelas}) - {self.hari}'


class JadwalPerkuliahanItem(models.Model):
    """Data jadwal perkuliahan yang diimpor murni dari file Excel"""
    semester = models.CharField(max_length=50, help_text="Contoh: Ganjil, Genap, atau 1, 2")
    kode_mk = models.CharField(max_length=30, verbose_name="Kode MK")
    nama_mk = models.CharField(max_length=300, verbose_name="Nama Mata Kuliah")
    sks = models.IntegerField(verbose_name="SKS")
    jadwal = models.CharField(max_length=300, blank=True, verbose_name="Jadwal Perkuliahan", help_text="Contoh: Senin 08:00-10:00")
    ruangan = models.CharField(max_length=100, blank=True, verbose_name="Ruangan", help_text="Contoh: R.Lab1")
    dosen = models.CharField(max_length=500, blank=True, verbose_name="Dosen Pengampu")
    kode_dosen = models.CharField(max_length=50, blank=True, verbose_name="Kode Dosen / NIDN")
    is_active = models.BooleanField(default=True)
    batch_label = models.CharField(max_length=100, blank=True, help_text="Label batch import, contoh: Genap 2025/2026")
    imported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Jadwal Perkuliahan Items'
        ordering = ['semester', 'kode_mk']

    def __str__(self):
        return f'{self.kode_mk} - {self.nama_mk} ({self.dosen})'


class KategoriBerkas(models.Model):
    """Kategori untuk Repository Berkas"""
    nama = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Kategori Berkas"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama


class RepositoryBerkas(models.Model):
    """Repository Berkas / Arsip Dokumen"""
    kategori = models.ForeignKey(KategoriBerkas, on_delete=models.CASCADE, related_name='berkas')
    nama_berkas = models.CharField(max_length=255)
    no_berkas = models.CharField(max_length=100, blank=True, null=True)
    perihal = models.TextField()
    tahun = models.IntegerField()
    file = models.FileField(upload_to='repository_berkas/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Repository Berkas"
        ordering = ['-tahun', '-created_at']

    def __str__(self):
        return f"{self.nama_berkas} ({self.tahun})"


# ============================================================
# Model dari Layanan Akademik (dikonsolidasi ke core)
# db_table tetap merujuk ke tabel lama agar data tidak hilang
# ============================================================

import datetime

def get_current_tahun_akademik():
    year = datetime.date.today().year
    month = datetime.date.today().month
    if month >= 9:
        return f"{year}/{year+1}"
    return f"{year-1}/{year}"


class Semester(models.Model):
    """Pengaturan Semester Gasal dan Genap"""
    JENIS_CHOICES = [
        ('gasal', 'Gasal'),
        ('genap', 'Genap'),
    ]
    tahun_akademik = models.CharField(max_length=20, default=get_current_tahun_akademik, help_text="Contoh: 2023/2024")
    jenis = models.CharField(max_length=10, choices=JENIS_CHOICES, default='gasal')
    is_active = models.BooleanField(default=False, help_text="Aktifkan untuk menandai semester berjalan")

    class Meta:
        db_table = 'layanan_akademik_semester'
        verbose_name_plural = "Data Semester"
        ordering = ['-tahun_akademik', '-jenis']

    def __str__(self):
        return f"{self.get_jenis_display()} {self.tahun_akademik}"


class Staf(models.Model):
    """Data Tendik / Karyawan"""
    nama = models.CharField(max_length=100)
    nip = models.CharField(max_length=50, blank=True, verbose_name="NIP/NIK")
    jabatan = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'layanan_akademik_staf'
        verbose_name_plural = "Data Staf (Tendik/Karyawan)"
        ordering = ['nama']

    def __str__(self):
        return self.nama


class Mahasiswa(models.Model):
    """Profil Mahasiswa"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mahasiswa_profile')
    nim = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100, blank=True, verbose_name="Program Studi")
    angkatan = models.IntegerField()
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'layanan_akademik_mahasiswa'
        verbose_name_plural = "Data Mahasiswa"
        ordering = ['nim']

    def save(self, *args, **kwargs):
        # Auto-create User if not exists
        if not self.user_id and self.nim:
            from django.contrib.auth.models import User as AuthUser
            user, created = AuthUser.objects.get_or_create(
                username=self.nim,
                defaults={
                    'first_name': self.nama[:30],
                    'is_active': True,
                    'is_staff': False,
                }
            )
            if created:
                user.set_password(self.nim)  # Default password: NIM
                user.save()
            self.user = user
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nim} - {self.nama}"



class KerjaPraktekMagang(models.Model):
    """Modul Kerja Praktek (KP) / Magang"""
    STATUS_CHOICES = [
        ('pengajuan', 'Pengajuan'),
        ('disetujui', 'Disetujui'),
        ('berjalan', 'Sedang Berjalan'),
        ('selesai', 'Selesai'),
        ('ditolak', 'Ditolak'),
    ]
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, related_name='kp_magang')
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)
    instansi_nama = models.CharField(max_length=200, verbose_name="Nama Perusahaan/Instansi")
    instansi_alamat = models.TextField(verbose_name="Alamat Instansi")
    dosen_pembimbing = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True, blank=True, related_name='bimbingan_kp')
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pengajuan')
    laporan_file = models.FileField(upload_to='layanan_akademik/kp/laporan/', blank=True, null=True)
    keterangan = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'layanan_akademik_kerjapraktekmagang'
        verbose_name_plural = "Kerja Praktek & Magang"
        ordering = ['-created_at']

    def __str__(self):
        return f"KP {self.mahasiswa.nama} - {self.instansi_nama}"


class TugasAkhir(models.Model):
    """Modul Tugas Akhir (Proposal & Skripsi)"""
    STATUS_TA_CHOICES = [
        ('judul', 'Pengajuan Judul'),
        ('proposal', 'Seminar Proposal'),
        ('skripsi', 'Sidang Skripsi'),
        ('lulus', 'Lulus / Selesai'),
    ]
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, related_name='tugas_akhir')
    judul = models.TextField()
    pembimbing_utama = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True, related_name='pembimbing_utama_ta')
    pembimbing_pendamping = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True, related_name='pembimbing_pendamping_ta')
    semester_mulai = models.ForeignKey(Semester, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS_TA_CHOICES, default='judul')
    metode_penelitian = models.TextField(blank=True, default='', verbose_name="Metode Penelitian")
    rumusan_masalah = models.TextField(blank=True, default='', verbose_name="Rumusan Masalah")
    pembimbing_usulan = models.CharField(max_length=200, blank=True, default='', verbose_name="Pembimbing Usulan")
    abstrak = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'layanan_akademik_tugasakhir'
        verbose_name_plural = "Tugas Akhir (Proposal & Skripsi)"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.mahasiswa.nim} - {self.mahasiswa.nama} ({self.judul[:50]})"


class KetuaSidang(models.Model):
    """Data Ketua Sidang/Seminar (Bisa Dosen atau Luar)"""
    nama = models.CharField(max_length=100)
    identitas = models.CharField(max_length=50, blank=True, verbose_name="NIP/NIK/NIDN")
    instansi = models.CharField(max_length=100, default="UNH", help_text="Asal instansi atau jabatan")

    class Meta:
        db_table = 'layanan_akademik_ketuasidang'
        verbose_name_plural = "Data Ketua Sidang/Seminar"
        ordering = ['nama']

    def __str__(self):
        return f"{self.nama} ({self.instansi})"


class SeminarProposal(models.Model):
    """Jadwal dan Hasil Seminar Proposal Skripsi"""
    HASIL_CHOICES = [
        ('pending', 'Belum Seminar'),
        ('lulus', 'Lulus'),
        ('revisi', 'Lulus dengan Revisi'),
        ('gagal', 'Tidak Lulus / Mengulang'),
    ]
    tugas_akhir = models.OneToOneField(TugasAkhir, on_delete=models.CASCADE, related_name='seminar_proposal',
                                        verbose_name="Mahasiswa",
                                        help_text="Cari berdasarkan NIM atau nama mahasiswa")
    tanggal = models.DateField()
    jam = models.TimeField()
    ruangan = models.CharField(max_length=100)

    # Tim Penguji Proposal
    ketua = models.ForeignKey(KetuaSidang, on_delete=models.SET_NULL, null=True, related_name='ketua_proposal', verbose_name="Ketua")
    penguji_utama = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True, related_name='penguji_utama_proposal', verbose_name="Penguji Utama")
    pembimbing_proposal = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True, related_name='pembimbing_proposal_ta', verbose_name="Pembimbing Proposal")
    notulis = models.ForeignKey(Staf, on_delete=models.SET_NULL, null=True, related_name='notulis_proposal_staf', verbose_name="Notulis (Tendik)")

    laporan_file = models.FileField(upload_to='layanan_akademik/ta/proposal/', blank=True, null=True)
    berita_acara = models.FileField(upload_to='layanan_akademik/ta/proposal/berita_acara/', blank=True, null=True)
    hasil = models.CharField(max_length=20, choices=HASIL_CHOICES, default='pending')
    catatan = models.TextField(blank=True)

    class Meta:
        db_table = 'layanan_akademik_seminarproposal'
        verbose_name = "Seminar Proposal"
        verbose_name_plural = "Jadwal Seminar Proposal"

    def __str__(self):
        return f"Seminar Proposal - {self.tugas_akhir.mahasiswa.nama}"


class SidangSkripsi(models.Model):
    """Jadwal dan Hasil Sidang Skripsi"""
    HASIL_CHOICES = [
        ('pending', 'Belum Sidang'),
        ('lulus', 'Lulus'),
        ('revisi', 'Lulus dengan Revisi'),
        ('gagal', 'Tidak Lulus / Mengulang'),
    ]
    tugas_akhir = models.OneToOneField(TugasAkhir, on_delete=models.CASCADE, related_name='sidang_skripsi')
    tanggal = models.DateField()
    jam = models.TimeField()
    ruangan = models.CharField(max_length=100)

    # Tim Penguji Sidang
    ketua = models.ForeignKey(KetuaSidang, on_delete=models.SET_NULL, null=True, related_name='ketua_sidang', verbose_name="Ketua")
    penguji_utama = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True, related_name='penguji_utama_sidang', verbose_name="Penguji Utama")
    pembimbing_utama = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True, related_name='pembimbing_utama_sidang', verbose_name="Pembimbing Utama")
    pembimbing_pendamping = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True, related_name='pembimbing_pendamping_sidang', verbose_name="Pembimbing Pendamping")
    notulis = models.ForeignKey(Staf, on_delete=models.SET_NULL, null=True, related_name='notulis_sidang_staf', verbose_name="Notulis (Tendik)")

    laporan_file = models.FileField(upload_to='layanan_akademik/ta/skripsi/', blank=True, null=True)
    berita_acara = models.FileField(upload_to='layanan_akademik/ta/skripsi/berita_acara/', blank=True, null=True)
    hasil = models.CharField(max_length=20, choices=HASIL_CHOICES, default='pending')
    catatan = models.TextField(blank=True)

    class Meta:
        db_table = 'layanan_akademik_sidangskripsi'
        verbose_name_plural = "Jadwal Sidang Skripsi"

    def __str__(self):
        return f"Sidang Skripsi - {self.tugas_akhir.mahasiswa.nama}"


class JudulProposalSkripsi(models.Model):
    """Pengajuan Judul Proposal Skripsi — Titik awal alur akademik"""
    STATUS_CHOICES = [
        ('pengajuan', 'Pengajuan (Menunggu Review)'),
        ('disetujui', 'Judul Disetujui'),
        ('bimbingan', 'Bimbingan Proposal'),
        ('seminar', 'Dijadwalkan Seminar'),
        ('lulus_seminar', 'Lulus Seminar Proposal'),
        ('skripsi', 'Terdaftar Tugas Akhir / Skripsi'),
        ('ditolak', 'Ditolak'),
    ]
    JUDUL_PILIHAN_CHOICES = [
        ('', '-- Belum Dipilih --'),
        ('1', 'Judul Proposal 1'),
        ('2', 'Judul Proposal 2'),
        ('3', 'Judul Proposal 3'),
    ]
    # Data Mahasiswa
    nim = models.CharField(max_length=20)
    nama_mahasiswa = models.CharField(max_length=100)
    program_studi = models.CharField(max_length=100)
    thn_akademik = models.CharField(max_length=50, verbose_name="Tahun Akademik")

    # 3 Judul Proposal
    judul_proposal1 = models.TextField(verbose_name="Judul Proposal 1")
    judul_proposal2 = models.TextField(verbose_name="Judul Proposal 2")
    judul_proposal3 = models.TextField(verbose_name="Judul Proposal 3")
    abstrak = models.TextField(blank=True)

    # Keputusan Tim (diisi admin)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pengajuan')
    judul_disetujui = models.CharField(max_length=1, choices=JUDUL_PILIHAN_CHOICES, blank=True, default='',
                                        verbose_name="Judul yang Disetujui",
                                        help_text="Pilih salah satu dari 3 judul yang diajukan")
    pembimbing_utama = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True, blank=True,
                                          related_name='pembimbing_utama_proposal', verbose_name="Pembimbing Utama")
    pembimbing_pendamping = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True, blank=True,
                                               related_name='pembimbing_pendamping_proposal', verbose_name="Pembimbing Pendamping")
    catatan_tim = models.TextField(blank=True, verbose_name="Catatan Tim / Kaprodi")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'layanan_akademik_judulproposalskripsi'
        verbose_name = "Pengajuan Judul Proposal"
        verbose_name_plural = "Pengajuan Judul Proposal Skripsi"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nim} - {self.nama_mahasiswa}"

    def get_judul_terpilih(self):
        """Mengembalikan teks judul yang disetujui"""
        if self.judul_disetujui == '1':
            return self.judul_proposal1
        elif self.judul_disetujui == '2':
            return self.judul_proposal2
        elif self.judul_disetujui == '3':
            return self.judul_proposal3
        return "Belum dipilih"



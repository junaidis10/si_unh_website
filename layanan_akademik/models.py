from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from core.models import Dosen

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
        verbose_name_plural = "Data Mahasiswa"
        ordering = ['nim']

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
    abstrak = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Tugas Akhir (Proposal & Skripsi)"
        ordering = ['-created_at']

    def __str__(self):
        return f"TA {self.mahasiswa.nim} - {self.mahasiswa.nama}"


class KetuaSidang(models.Model):
    """Data Ketua Sidang/Seminar (Bisa Dosen atau Luar)"""
    nama = models.CharField(max_length=100)
    identitas = models.CharField(max_length=50, blank=True, verbose_name="NIP/NIK/NIDN")
    instansi = models.CharField(max_length=100, default="UNH", help_text="Asal instansi atau jabatan")

    class Meta:
        verbose_name_plural = "Data Ketua Sidang/Seminar"
        ordering = ['nama']

    def __str__(self):
        return f"{self.nama} ({self.instansi})"


class SeminarProposal(models.Model):
    """Jadwal dan Hasil Seminar Proposal"""
    HASIL_CHOICES = [
        ('pending', 'Belum Seminar'),
        ('lulus', 'Lulus'),
        ('revisi', 'Lulus dengan Revisi'),
        ('gagal', 'Tidak Lulus / Mengulang'),
    ]
    tugas_akhir = models.OneToOneField(TugasAkhir, on_delete=models.CASCADE, related_name='seminar_proposal')
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
        verbose_name_plural = "Jadwal Sidang Skripsi"

    def __str__(self):
        return f"Sidang Skripsi - {self.tugas_akhir.mahasiswa.nama}"

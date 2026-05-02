from django.contrib import admin
from .models import Semester, Staf, KetuaSidang, Mahasiswa, KerjaPraktekMagang, TugasAkhir, SeminarProposal, SidangSkripsi

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('tahun_akademik', 'jenis', 'is_active')
    list_filter = ('jenis', 'is_active')
    search_fields = ('tahun_akademik',)

@admin.register(Staf)
class StafAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nip', 'jabatan', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nama', 'nip')

@admin.register(KetuaSidang)
class KetuaSidangAdmin(admin.ModelAdmin):
    list_display = ('nama', 'identitas', 'instansi')
    search_fields = ('nama', 'identitas', 'instansi')

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('nim', 'nama', 'prodi', 'angkatan', 'is_active')
    list_filter = ('angkatan', 'prodi', 'is_active')
    search_fields = ('nim', 'nama')
    change_list_template = "admin/layanan_akademik/mahasiswa_changelist.html"

@admin.register(KerjaPraktekMagang)
class KerjaPraktekMagangAdmin(admin.ModelAdmin):
    list_display = ('mahasiswa', 'instansi_nama', 'semester', 'status', 'dosen_pembimbing')
    list_filter = ('status', 'semester')
    search_fields = ('mahasiswa__nama', 'instansi_nama')
    autocomplete_fields = ['mahasiswa', 'dosen_pembimbing']

@admin.register(TugasAkhir)
class TugasAkhirAdmin(admin.ModelAdmin):
    list_display = ('mahasiswa', 'judul', 'status', 'pembimbing_utama')
    list_filter = ('status', 'semester_mulai')
    search_fields = ('mahasiswa__nama', 'judul')
    autocomplete_fields = ['mahasiswa', 'pembimbing_utama', 'pembimbing_pendamping']

@admin.register(SeminarProposal)
class SeminarProposalAdmin(admin.ModelAdmin):
    list_display = ('tugas_akhir', 'tanggal', 'jam', 'ruangan', 'hasil')
    list_filter = ('hasil', 'tanggal')
    search_fields = ('tugas_akhir__mahasiswa__nama',)
    autocomplete_fields = ['tugas_akhir', 'ketua', 'penguji_utama', 'pembimbing_proposal', 'notulis']

@admin.register(SidangSkripsi)
class SidangSkripsiAdmin(admin.ModelAdmin):
    list_display = ('tugas_akhir', 'tanggal', 'jam', 'ruangan', 'hasil')
    list_filter = ('hasil', 'tanggal')
    search_fields = ('tugas_akhir__mahasiswa__nama',)
    autocomplete_fields = ['tugas_akhir', 'ketua', 'penguji_utama', 'pembimbing_utama', 'pembimbing_pendamping', 'notulis']

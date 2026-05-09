from django.contrib import admin
from .models import *

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']


@admin.register(Sambutan)
class SambutanAdmin(admin.ModelAdmin):
    list_display = ['ketua_name', 'jabatan', 'is_active', 'updated_at']
    list_filter = ['is_active']


@admin.register(VisiMisi)
class VisiMisiAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'updated_at']


@admin.register(ProspekKeunggulan)
class ProspekKeunggulanAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']


@admin.register(Dosen)
class DosenAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nidn', 'kategori', 'pendidikan', 'is_active', 'action_tarik_sinta']
    list_filter = ['kategori', 'is_active']
    search_fields = ['nama', 'nidn', 'email', 'bidang_keahlian']
    list_editable = ['is_active']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.username in ['junaidisurya', 'ahmad husna ahadi']:
            return qs
        return qs.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        if request.user.is_superuser or request.user.username in ['junaidisurya', 'ahmad husna ahadi']:
            return True
        return obj.user == request.user

    def action_tarik_sinta(self, obj):
        from django.utils.html import format_html
        if obj.sinta_link:
            return format_html('<a class="button" style="background-color: #28a745; color: white; padding: 5px 10px; border-radius: 4px;" href="/admin-tools/tarik-sinta/{}/">Tarik Data Sinta</a>', obj.id)
        return "-"
    action_tarik_sinta.short_description = 'Aksi Sinta'


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'uploaded_by', 'uploaded_at', 'download_count', 'is_active']
    list_filter = ['category', 'is_active', 'uploaded_at']
    search_fields = ['title', 'description']
    readonly_fields = ['download_count', 'uploaded_at']
    list_editable = ['is_active']
@admin.register(BukuPanduan)
class BukuPanduanAdmin(admin.ModelAdmin):
    list_display = ['title','description', 'uploaded_at', 'download_count', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    readonly_fields = ['download_count', 'uploaded_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(category__slug='buku-panduan')

    def save_model(self, request, obj, form, change):
        # Automatically assign to Buku Panduan category if not set
        if not obj.category_id:
            try:
                cat = DocumentCategory.objects.get(slug='buku-panduan')
                obj.category = cat
            except DocumentCategory.DoesNotExist:
                pass
        super().save_model(request, obj, form, change)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'views', 'is_featured', 'is_published']
    list_filter = ['is_featured', 'is_published', 'published_date']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['views', 'published_date']
    list_editable = ['is_featured', 'is_published']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'media_type', 'uploaded_at', 'is_active']
    list_filter = ['media_type', 'is_active', 'uploaded_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active']


@admin.register(Prestasi)
class PrestasiAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'achievement', 'tingkat', 'year', 'date_achieved']
    list_filter = ['tingkat', 'year']
    search_fields = ['student_name', 'achievement']


@admin.register(Penelitian)
class PenelitianAdmin(admin.ModelAdmin):
    list_display = ['title', 'jenis', 'tipe_peneliti', 'year', 'peneliti', 'owner']
    list_filter = ['jenis', 'tipe_peneliti', 'year']
    search_fields = ['title', 'peneliti', 'abstrak']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.username in ['junaidisurya', 'ahmad husna ahadi']:
            return qs
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not (request.user.is_superuser or request.user.username in ['junaidisurya', 'ahmad husna ahadi']):
            if 'owner' in fields:
                fields.remove('owner')
        return fields


@admin.register(Akreditasi)
class AkreditasiAdmin(admin.ModelAdmin):
    list_display = ['program', 'peringkat', 'nomor_sk', 'tanggal_sk', 'masa_berlaku', 'is_active']
    list_filter = ['is_active', 'lembaga']
    list_editable = ['is_active']


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ['nama', 'tahun_lulus', 'pekerjaan', 'perusahaan', 'testimoni_short']
    list_filter = ['tahun_lulus']
    search_fields = ['nama', 'nim', 'pekerjaan', 'perusahaan', 'testimoni']
    
    fieldsets = (
        (None, {
            'fields': ('nama', 'nim', 'tahun_lulus', 'photo')
        }),
        ('Karir', {
            'fields': ('pekerjaan', 'perusahaan', 'linkedin')
        }),
        ('Kontak', {
            'fields': ('email', 'phone')
        }),
        ('Testimoni', {
            'fields': ('testimoni',)
        }),
    )

    def testimoni_short(self, obj):
        if obj.testimoni:
            return obj.testimoni[:50] + "..." if len(obj.testimoni) > 50 else obj.testimoni
        return "-"
    testimoni_short.short_description = 'Testimoni'


@admin.register(JobCareer)
class JobCareerAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'location', 'application_deadline', 'is_active', 'posted_date']
    list_filter = ['is_active', 'posted_date', 'job_type']
    search_fields = ['position', 'company', 'description']
    list_editable = ['is_active']


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'kategori', 'url', 'order', 'is_active']
    list_filter = ['kategori', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'title', 'updated_at']
    search_fields = ['page_name', 'title', 'content']
@admin.register(MataKuliah)
class MataKuliahAdmin(admin.ModelAdmin):
    list_display = ['kode', 'nama', 'semester', 'sks', 'is_active']
    list_filter = ['semester', 'kategori', 'is_active']
    search_fields = ['kode', 'nama', 'dosen_pengampu__nama']
    list_editable = ['is_active']
    filter_horizontal = ('dosen_pengampu',)
    
    fieldsets = [
        (None, {
            'fields': ('kode', 'nama', 'sks', 'semester', 'kategori', 'order', 'is_active')
        }),
        ('Informasi RPS & Perkuliahan', {
            'fields': ('rps_document', 'dosen_pengampu', 'materi_perkuliahan', 'dosen_pengampu_legacy')
        }),
        ('Deskripsi', {
            'fields': ('deskripsi',),
            'classes': ('collapse',)
        }),
    ]

    def rps_link_status(self, obj):
        if obj.rps_document:
            return "✅ Tersedia"
        return "❌ Kosong"
    rps_link_status.short_description = 'RPS'

    def dosen_count(self, obj):
        return obj.dosen_pengampu.count()
    dosen_count.short_description = 'Jml Dosen'

@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ['status', 'lama_bergabung', 'tingkat_paham', 'created_at']
    list_filter = ['status', 'tingkat_paham', 'created_at']
    search_fields = ['status', 'saran_kritik']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Identitas', {
            'fields': ('status', 'lama_bergabung')
        }),
        ('Sosialisasi', {
            'fields': ('pengetahuan_visi', 'sumber_informasi', 'frekuensi_sosialisasi')
        }),
        ('Pemahaman & Analisis', {
            'fields': ('tingkat_paham', 'aspek_tercermin', 'bidang_tercermin', 'dukungan_atmosfer', 'perlu_perbaikan')
        }),
        ('Evaluasi', {
            'fields': ('saran_kritik', 'created_at')
        }),
    )

@admin.register(SurveyKepuasanLulusan)
class SurveyKepuasanLulusanAdmin(admin.ModelAdmin):
    list_display = ['nama_instansi', 'nama_responden', 'jabatan', 'waktu_tunggu', 'created_at']
    list_filter = ['waktu_tunggu', 'created_at']
    search_fields = ['nama_instansi', 'nama_responden', 'email']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Identitas Perusahaan', {
            'fields': ('email', 'nama_responden', 'nama_instansi', 'jabatan')
        }),
        ('Penilaian Kompetensi', {
            'fields': (
                'integritas', 'keahlian_bidang', 'bahasa_inggris', 
                'penggunaan_it', 'komunikasi', 'kerjasama_tim', 'pengembangan_diri'
            )
        }),
        ('Indikator Kerja', {
            'fields': ('waktu_tunggu', 'created_at')
        }),
    )

@admin.register(SurveyKurikulum)
class SurveyKurikulumAdmin(admin.ModelAdmin):
    list_display = ['nama_responden', 'kategori_responden', 'instansi', 'created_at']
    list_filter = ['kategori_responden', 'created_at']
    search_fields = ['nama_responden', 'instansi', 'responses_data']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Identitas Responden', {
            'fields': ('nama_responden', 'kategori_responden', 'instansi', 'jabatan', 'email')
        }),
        ('Data Kuesioner', {
            'fields': ('responses_data', 'created_at')
        }),
    )

@admin.register(JadwalKuliah)
class JadwalKuliahAdmin(admin.ModelAdmin):
    list_display = ['mata_kuliah', 'kelas', 'hari', 'jam_mulai', 'jam_selesai', 'ruangan', 'is_active']
    list_filter = ['hari', 'is_active', 'mata_kuliah__semester']
    search_fields = ['mata_kuliah__nama', 'kelas', 'ruangan']
    list_editable = ['is_active', 'ruangan', 'hari', 'jam_mulai', 'jam_selesai']
    filter_horizontal = ('dosen_pengampu',)


@admin.register(JadwalPerkuliahanItem)
class JadwalPerkuliahanItemAdmin(admin.ModelAdmin):
    list_display = ['semester', 'kode_mk', 'nama_mk', 'sks', 'jadwal', 'ruangan', 'dosen', 'batch_label', 'is_active']
    list_filter = ['semester', 'is_active', 'batch_label']
    search_fields = ['kode_mk', 'nama_mk', 'dosen', 'jadwal', 'ruangan']
    list_editable = ['is_active', 'jadwal', 'ruangan']


@admin.register(KategoriBerkas)
class KategoriBerkasAdmin(admin.ModelAdmin):
    list_display = ['nama', 'slug']
    prepopulated_fields = {'slug': ('nama',)}


@admin.register(RepositoryBerkas)
class RepositoryBerkasAdmin(admin.ModelAdmin):
    list_display = ['nama_berkas', 'no_berkas', 'kategori', 'tahun', 'created_at']
    list_filter = ['kategori', 'tahun']
    search_fields = ['nama_berkas', 'no_berkas', 'perihal']


# ============================================================
# Admin Layanan Akademik (dikonsolidasi dari layanan_akademik app)
# ============================================================

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
# ============================================================
# ALUR: JudulProposal → TugasAkhir → Seminar Proposal → Sidang
# ============================================================

# Inline Seminar Proposal di dalam TugasAkhir
class SeminarProposalInline(admin.StackedInline):
    model = SeminarProposal
    extra = 0
    max_num = 1
    verbose_name = "Penjadwalan Seminar Proposal"
    verbose_name_plural = "Penjadwalan Seminar Proposal"
    autocomplete_fields = ['ketua', 'penguji_utama', 'pembimbing_proposal', 'notulis']
    fieldsets = (
        ('Jadwal', {
            'fields': ('tanggal', 'jam', 'ruangan')
        }),
        ('Tim Penguji', {
            'fields': ('ketua', 'penguji_utama', 'pembimbing_proposal', 'notulis')
        }),
        ('Hasil Seminar', {
            'fields': ('hasil', 'catatan', 'laporan_file', 'berita_acara')
        }),
    )

# Inline Sidang Skripsi di dalam TugasAkhir
class SidangSkripsiInline(admin.StackedInline):
    model = SidangSkripsi
    extra = 0
    max_num = 1
    verbose_name = "Penjadwalan Sidang Skripsi"
    verbose_name_plural = "Penjadwalan Sidang Skripsi"
    autocomplete_fields = ['ketua', 'penguji_utama', 'pembimbing_utama', 'pembimbing_pendamping', 'notulis']


# --- 1. PENGAJUAN JUDUL PROPOSAL (Titik awal alur) ---
@admin.register(JudulProposalSkripsi)
class JudulProposalSkripsiAdmin(admin.ModelAdmin):
    list_display = ('nim', 'nama_mahasiswa', 'program_studi', 'thn_akademik', 'status', 'judul_disetujui_display', 'created_at')
    list_filter = ('status', 'program_studi', 'thn_akademik')
    search_fields = ('nim', 'nama_mahasiswa', 'judul_proposal1', 'judul_proposal2', 'judul_proposal3')
    readonly_fields = ('created_at',)
    autocomplete_fields = ['pembimbing_utama', 'pembimbing_pendamping']

    fieldsets = (
        ('Data Mahasiswa', {
            'fields': ('nim', 'nama_mahasiswa', 'program_studi', 'thn_akademik', 'created_at')
        }),
        ('3 Judul Proposal yang Diajukan', {
            'fields': ('judul_proposal1', 'judul_proposal2', 'judul_proposal3', 'abstrak')
        }),
        ('Keputusan Tim / Kaprodi', {
            'fields': ('status', 'judul_disetujui', 'pembimbing_utama', 'pembimbing_pendamping', 'catatan_tim'),
            'description': '⬇️ Pilih salah satu judul, tentukan pembimbing, ubah status. Setelah disetujui, buat Tugas Akhir untuk jadwalkan seminar.',
        }),
    )

    def judul_disetujui_display(self, obj):
        if obj.judul_disetujui:
            return f"Judul {obj.judul_disetujui}"
        return "—"
    judul_disetujui_display.short_description = "Judul Dipilih"


# --- 2. TUGAS AKHIR + SEMINAR + SIDANG (All-in-one) ---
@admin.register(TugasAkhir)
class TugasAkhirAdmin(admin.ModelAdmin):
    list_display = ('mahasiswa', 'judul', 'status', 'pembimbing_utama')
    list_filter = ('status', 'semester_mulai')
    search_fields = ('mahasiswa__nama', 'mahasiswa__nim', 'judul')
    autocomplete_fields = ['mahasiswa', 'pembimbing_utama', 'pembimbing_pendamping', 'semester_mulai']
    inlines = [SeminarProposalInline, SidangSkripsiInline]

    fieldsets = (
        ('Data Mahasiswa & Judul Skripsi', {
            'fields': ('mahasiswa', 'judul', 'semester_mulai', 'status')
        }),
        ('Pembimbing', {
            'fields': ('pembimbing_utama', 'pembimbing_pendamping', 'pembimbing_usulan')
        }),
        ('Detail', {
            'fields': ('abstrak', 'rumusan_masalah', 'metode_penelitian'),
            'classes': ('collapse',),
        }),
    )

    def save_formset(self, request, form, formset, change):
        """Auto-update status TA berdasarkan hasil seminar/sidang"""
        instances = formset.save()
        for obj in instances:
            if isinstance(obj, SeminarProposal):
                ta = obj.tugas_akhir
                if obj.hasil in ['lulus', 'revisi']:
                    if ta.status in ['judul', 'proposal']:
                        ta.status = 'skripsi'
                        ta.save()
                elif obj.hasil == 'pending' and ta.status == 'judul':
                    ta.status = 'proposal'
                    ta.save()

# --- 3. SEMINAR PROPOSAL (Standalone — ambil dari Pengajuan Judul) ---
from django import forms
from django.contrib.auth.models import User

class SeminarProposalAdminForm(forms.ModelForm):
    """Form custom: admin pilih mahasiswa dari daftar pengajuan judul proposal"""
    pengajuan_judul = forms.ModelChoiceField(
        queryset=JudulProposalSkripsi.objects.all(),
        label="Mahasiswa (Pengajuan Judul Proposal)",
        help_text="Pilih mahasiswa yang sudah mengajukan judul proposal",
        required=True,
    )

    class Meta:
        model = SeminarProposal
        fields = ['pengajuan_judul', 'tanggal', 'jam', 'ruangan',
                  'ketua', 'penguji_utama', 'pembimbing_proposal', 'notulis',
                  'hasil', 'catatan', 'laporan_file', 'berita_acara']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Jika editing, cari proposal yang sesuai dengan tugas_akhir
        if self.instance.pk and self.instance.tugas_akhir_id:
            try:
                nim = self.instance.tugas_akhir.mahasiswa.nim
                jp = JudulProposalSkripsi.objects.filter(nim=nim).first()
                if jp:
                    self.initial['pengajuan_judul'] = jp.pk
            except Exception:
                pass

    def save(self, commit=True):
        instance = super().save(commit=False)
        proposal = self.cleaned_data['pengajuan_judul']

        # 1. Cari atau buat User
        user, _ = User.objects.get_or_create(
            username=proposal.nim,
            defaults={
                'first_name': proposal.nama_mahasiswa,
                'is_active': True,
            }
        )

        # 2. Cari atau buat Mahasiswa
        mhs, _ = Mahasiswa.objects.get_or_create(
            nim=proposal.nim,
            defaults={
                'user': user,
                'nama': proposal.nama_mahasiswa,
                'prodi': proposal.program_studi,
                'angkatan': int(proposal.thn_akademik[:4]) if proposal.thn_akademik else 2024,
            }
        )

        # 3. Cari atau buat Semester
        semester = Semester.objects.filter(is_active=True).first()
        if not semester:
            semester, _ = Semester.objects.get_or_create(
                tahun_akademik=proposal.thn_akademik,
                defaults={'jenis': 'gasal', 'is_active': True}
            )

        # 4. Cari atau buat TugasAkhir
        judul_terpilih = proposal.get_judul_terpilih()
        ta, created = TugasAkhir.objects.get_or_create(
            mahasiswa=mhs,
            defaults={
                'judul': judul_terpilih,
                'semester_mulai': semester,
                'status': 'proposal',
            }
        )
        if created and hasattr(proposal, 'pembimbing_utama') and proposal.pembimbing_utama:
            ta.pembimbing_utama = proposal.pembimbing_utama
            ta.pembimbing_pendamping = proposal.pembimbing_pendamping
            ta.save()

        # Update status proposal
        proposal.status = 'seminar'
        proposal.save()

        instance.tugas_akhir = ta
        if commit:
            instance.save()
        return instance


@admin.register(SeminarProposal)
class SeminarProposalAdmin(admin.ModelAdmin):
    form = SeminarProposalAdminForm
    list_display = ('get_mahasiswa', 'get_nim', 'tanggal', 'jam', 'ruangan', 'hasil')
    list_filter = ('hasil', 'tanggal')
    search_fields = ('tugas_akhir__mahasiswa__nama', 'tugas_akhir__mahasiswa__nim')
    autocomplete_fields = ['ketua', 'penguji_utama', 'pembimbing_proposal', 'notulis']

    fieldsets = (
        ('Mahasiswa', {
            'fields': ('pengajuan_judul',),
            'description': '📋 Pilih mahasiswa dari daftar pengajuan judul proposal.',
        }),
        ('Jadwal Seminar', {
            'fields': ('tanggal', 'jam', 'ruangan')
        }),
        ('Tim Penguji', {
            'fields': ('ketua', 'penguji_utama', 'pembimbing_proposal', 'notulis')
        }),
        ('Hasil Seminar', {
            'fields': ('hasil', 'catatan', 'laporan_file', 'berita_acara'),
            'classes': ('collapse',),
        }),
    )

    def get_mahasiswa(self, obj):
        return obj.tugas_akhir.mahasiswa.nama
    get_mahasiswa.short_description = "Nama Mahasiswa"

    def get_nim(self, obj):
        return obj.tugas_akhir.mahasiswa.nim
    get_nim.short_description = "NIM"

# --- 4. SIDANG SKRIPSI (Standalone list) ---
@admin.register(SidangSkripsi)
class SidangSkripsiAdmin(admin.ModelAdmin):
    list_display = ('tugas_akhir', 'tanggal', 'jam', 'ruangan', 'hasil')
    list_filter = ('hasil', 'tanggal')
    search_fields = ('tugas_akhir__mahasiswa__nama',)
    autocomplete_fields = ['tugas_akhir', 'ketua', 'penguji_utama', 'pembimbing_utama', 'pembimbing_pendamping', 'notulis']

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
    list_display = ['nama', 'nidn', 'kategori', 'pendidikan', 'is_active']
    list_filter = ['kategori', 'is_active']
    search_fields = ['nama', 'nidn', 'email', 'bidang_keahlian']
    list_editable = ['is_active']


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
    list_display = ['title', 'jenis', 'year', 'peneliti']
    list_filter = ['jenis', 'year']
    search_fields = ['title', 'peneliti', 'abstrak']


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

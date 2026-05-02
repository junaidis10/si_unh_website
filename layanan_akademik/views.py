from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db import DatabaseError, transaction
import pandas as pd
from .models import Semester, Mahasiswa, KerjaPraktekMagang, TugasAkhir, SeminarProposal, SidangSkripsi

class MahasiswaImportView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_staff:
            messages.error(request, "Akses ditolak.")
            return redirect('layanan_akademik:dashboard')
        return render(request, 'layanan_akademik/import_mahasiswa.html')

    def post(self, request):
        if not request.user.is_staff:
            return redirect('layanan_akademik:dashboard')
            
        excel_file = request.FILES.get('file')
        if not excel_file:
            messages.error(request, "Silakan pilih file excel.")
            return redirect('layanan_akademik:mahasiswa_import')

        try:
            df = pd.read_excel(excel_file)
            # Normalisasi kolom
            df.columns = [c.lower().strip() for c in df.columns]
            
            required_cols = ['nim', 'nama', 'program studi', 'angkatan']
            for col in required_cols:
                if col not in df.columns:
                    messages.error(request, f"Kolom '{col}' tidak ditemukan dalam file.")
                    return redirect('layanan_akademik:mahasiswa_import')

            count = 0
            with transaction.atomic():
                for _, row in df.iterrows():
                    nim = str(row['nim']).strip()
                    nama = str(row['nama']).strip()
                    prodi = str(row['program studi']).strip()
                    angkatan = int(row['angkatan'])

                    # Buat User jika belum ada
                    user, created = User.objects.get_or_create(
                        username=nim,
                        defaults={
                            'first_name': nama[:30],
                            'is_active': True
                        }
                    )
                    if created:
                        user.set_password(nim) # Default password adalah NIM
                        user.save()

                    # Buat Mahasiswa
                    Mahasiswa.objects.update_or_create(
                        nim=nim,
                        defaults={
                            'user': user,
                            'nama': nama,
                            'prodi': prodi,
                            'angkatan': angkatan
                        }
                    )
                    count += 1

            messages.success(request, f"Berhasil mengimpor {count} data mahasiswa.")
            return redirect('/Js0312yA11/layanan_akademik/mahasiswa/')

        except Exception as e:
            messages.error(request, f"Gagal mengimpor data: {str(e)}")
            return redirect('layanan_akademik:mahasiswa_import')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'layanan_akademik/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            # Ambil semester aktif
            semester_qs = Semester.objects.filter(is_active=True)
            context['semester_aktif'] = semester_qs.first() if semester_qs.exists() else None
            
            # Jika user adalah mahasiswa, ambil datanya
            try:
                if hasattr(self.request.user, 'mahasiswa_profile'):
                    context['mhs'] = self.request.user.mahasiswa_profile
                    # Force evaluation to catch 1146 error here
                    context['kp_status'] = list(KerjaPraktekMagang.objects.filter(mahasiswa=context['mhs'])[:1])
                    context['kp_status'] = context['kp_status'][0] if context['kp_status'] else None
                    
                    context['ta_status'] = list(TugasAkhir.objects.filter(mahasiswa=context['mhs'])[:1])
                    context['ta_status'] = context['ta_status'][0] if context['ta_status'] else None
                    
                    if context['ta_status']:
                        # Ambil info seminar dan sidang khusus mahasiswa ini
                        context['seminar_mhs'] = SeminarProposal.objects.filter(tugas_akhir=context['ta_status']).first()
                        context['sidang_mhs'] = SidangSkripsi.objects.filter(tugas_akhir=context['ta_status']).first()
                else:
                    context['mhs'] = None
            except (DatabaseError, AttributeError):
                context['mhs'] = None
        except DatabaseError:
            context['db_error'] = True
            context['semester_aktif'] = None
            context['mhs'] = None
            
        return context

class KPListView(LoginRequiredMixin, ListView):
    model = KerjaPraktekMagang
    template_name = 'layanan_akademik/kp_list.html'
    context_object_name = 'kp_list'

    def get_queryset(self):
        try:
            # Mahasiswa hanya melihat miliknya, dosen/admin melihat semua
            if hasattr(self.request.user, 'mahasiswa_profile'):
                return KerjaPraktekMagang.objects.filter(mahasiswa=self.request.user.mahasiswa_profile)
            return KerjaPraktekMagang.objects.all()
        except DatabaseError:
            return KerjaPraktekMagang.objects.none()

class KPCreateView(LoginRequiredMixin, CreateView):
    model = KerjaPraktekMagang
    template_name = 'layanan_akademik/kp_form.html'
    fields = ['semester', 'instansi_nama', 'instansi_alamat', 'tanggal_mulai', 'tanggal_selesai']
    success_url = reverse_lazy('layanan_akademik:kp_list')

    def form_valid(self, form):
        try:
            form.instance.mahasiswa = self.request.user.mahasiswa_profile
            return super().form_valid(form)
        except DatabaseError:
            return redirect('layanan_akademik:dashboard')

class TAListView(LoginRequiredMixin, ListView):
    model = TugasAkhir
    template_name = 'layanan_akademik/ta_list.html'
    context_object_name = 'ta_list'
    
    def get_queryset(self):
        try:
            if hasattr(self.request.user, 'mahasiswa_profile'):
                return TugasAkhir.objects.filter(mahasiswa=self.request.user.mahasiswa_profile)
            return TugasAkhir.objects.all()
        except DatabaseError:
            return TugasAkhir.objects.none()

class TACreateView(LoginRequiredMixin, CreateView):
    model = TugasAkhir
    template_name = 'layanan_akademik/ta_form.html'
    fields = ['judul', 'semester_mulai', 'abstrak']
    success_url = reverse_lazy('layanan_akademik:ta_list')

    def form_valid(self, form):
        try:
            form.instance.mahasiswa = self.request.user.mahasiswa_profile
            return super().form_valid(form)
        except DatabaseError:
            return redirect('layanan_akademik:dashboard')

class JadwalView(LoginRequiredMixin, TemplateView):
    template_name = 'layanan_akademik/jadwal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            # Force evaluation with list() to catch DatabaseError here, not in template
            context['seminar_proposal'] = list(SeminarProposal.objects.all().order_by('tanggal', 'jam'))
            context['sidang_skripsi'] = list(SidangSkripsi.objects.all().order_by('tanggal', 'jam'))
        except DatabaseError:
            context['seminar_proposal'] = []
            context['sidang_skripsi'] = []
            context['db_error'] = True
        return context

"""
Migration: Register layanan_akademik models in core app state.
Tables already exist in DB from layanan_akademik migrations.
Uses SeparateDatabaseAndState so no actual DB operations happen.
"""
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_kategoriberkas_repositoryberkas'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Semester',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('tahun_akademik', models.CharField(max_length=20)),
                        ('jenis', models.CharField(choices=[('gasal', 'Gasal'), ('genap', 'Genap')], default='gasal', max_length=10)),
                        ('is_active', models.BooleanField(default=False)),
                    ],
                    options={'db_table': 'layanan_akademik_semester', 'verbose_name_plural': 'Data Semester', 'ordering': ['-tahun_akademik', '-jenis']},
                ),
                migrations.CreateModel(
                    name='Staf',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('nama', models.CharField(max_length=100)),
                        ('nip', models.CharField(blank=True, max_length=50)),
                        ('jabatan', models.CharField(blank=True, max_length=100)),
                        ('is_active', models.BooleanField(default=True)),
                    ],
                    options={'db_table': 'layanan_akademik_staf', 'verbose_name_plural': 'Data Staf (Tendik/Karyawan)', 'ordering': ['nama']},
                ),
                migrations.CreateModel(
                    name='KetuaSidang',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('nama', models.CharField(max_length=100)),
                        ('identitas', models.CharField(blank=True, max_length=50)),
                        ('instansi', models.CharField(default='UNH', max_length=100)),
                    ],
                    options={'db_table': 'layanan_akademik_ketuasidang', 'verbose_name_plural': 'Data Ketua Sidang/Seminar', 'ordering': ['nama']},
                ),
                migrations.CreateModel(
                    name='Mahasiswa',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('nim', models.CharField(max_length=20, unique=True)),
                        ('nama', models.CharField(max_length=100)),
                        ('prodi', models.CharField(blank=True, max_length=100)),
                        ('angkatan', models.IntegerField()),
                        ('phone', models.CharField(blank=True, max_length=20)),
                        ('is_active', models.BooleanField(default=True)),
                        ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mahasiswa_profile', to=settings.AUTH_USER_MODEL)),
                    ],
                    options={'db_table': 'layanan_akademik_mahasiswa', 'verbose_name_plural': 'Data Mahasiswa', 'ordering': ['nim']},
                ),
                migrations.CreateModel(
                    name='KerjaPraktekMagang',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('instansi_nama', models.CharField(max_length=200)),
                        ('instansi_alamat', models.TextField()),
                        ('tanggal_mulai', models.DateField()),
                        ('tanggal_selesai', models.DateField()),
                        ('status', models.CharField(choices=[('pengajuan', 'Pengajuan'), ('disetujui', 'Disetujui'), ('berjalan', 'Sedang Berjalan'), ('selesai', 'Selesai'), ('ditolak', 'Ditolak')], default='pengajuan', max_length=20)),
                        ('laporan_file', models.FileField(blank=True, null=True, upload_to='layanan_akademik/kp/laporan/')),
                        ('keterangan', models.TextField(blank=True)),
                        ('created_at', models.DateTimeField(auto_now_add=True)),
                        ('dosen_pembimbing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bimbingan_kp', to='core.dosen')),
                        ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kp_magang', to='core.mahasiswa')),
                        ('semester', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.semester')),
                    ],
                    options={'db_table': 'layanan_akademik_kerjapraktekmagang', 'verbose_name_plural': 'Kerja Praktek & Magang', 'ordering': ['-created_at']},
                ),
                migrations.CreateModel(
                    name='TugasAkhir',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('judul', models.TextField()),
                        ('status', models.CharField(choices=[('judul', 'Pengajuan Judul'), ('proposal', 'Seminar Proposal'), ('skripsi', 'Sidang Skripsi'), ('lulus', 'Lulus / Selesai')], default='judul', max_length=20)),
                        ('abstrak', models.TextField(blank=True)),
                        ('is_active', models.BooleanField(default=True)),
                        ('created_at', models.DateTimeField(auto_now_add=True)),
                        ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tugas_akhir', to='core.mahasiswa')),
                        ('pembimbing_utama', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pembimbing_utama_ta', to='core.dosen')),
                        ('pembimbing_pendamping', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pembimbing_pendamping_ta', to='core.dosen')),
                        ('semester_mulai', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.semester')),
                    ],
                    options={'db_table': 'layanan_akademik_tugasakhir', 'verbose_name_plural': 'Tugas Akhir (Proposal & Skripsi)', 'ordering': ['-created_at']},
                ),
                migrations.CreateModel(
                    name='SeminarProposal',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('tanggal', models.DateField()),
                        ('jam', models.TimeField()),
                        ('ruangan', models.CharField(max_length=100)),
                        ('laporan_file', models.FileField(blank=True, null=True, upload_to='layanan_akademik/ta/proposal/')),
                        ('berita_acara', models.FileField(blank=True, null=True, upload_to='layanan_akademik/ta/proposal/berita_acara/')),
                        ('hasil', models.CharField(choices=[('pending', 'Belum Seminar'), ('lulus', 'Lulus'), ('revisi', 'Lulus dengan Revisi'), ('gagal', 'Tidak Lulus / Mengulang')], default='pending', max_length=20)),
                        ('catatan', models.TextField(blank=True)),
                        ('tugas_akhir', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seminar_proposal', to='core.tugasakhir')),
                        ('ketua', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ketua_proposal', to='core.ketuasidang')),
                        ('penguji_utama', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='penguji_utama_proposal', to='core.dosen')),
                        ('pembimbing_proposal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pembimbing_proposal_ta', to='core.dosen')),
                        ('notulis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notulis_proposal_staf', to='core.staf')),
                    ],
                    options={'db_table': 'layanan_akademik_seminarproposal', 'verbose_name_plural': 'Jadwal Seminar Proposal'},
                ),
                migrations.CreateModel(
                    name='SidangSkripsi',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('tanggal', models.DateField()),
                        ('jam', models.TimeField()),
                        ('ruangan', models.CharField(max_length=100)),
                        ('laporan_file', models.FileField(blank=True, null=True, upload_to='layanan_akademik/ta/skripsi/')),
                        ('berita_acara', models.FileField(blank=True, null=True, upload_to='layanan_akademik/ta/skripsi/berita_acara/')),
                        ('hasil', models.CharField(choices=[('pending', 'Belum Sidang'), ('lulus', 'Lulus'), ('revisi', 'Lulus dengan Revisi'), ('gagal', 'Tidak Lulus / Mengulang')], default='pending', max_length=20)),
                        ('catatan', models.TextField(blank=True)),
                        ('tugas_akhir', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sidang_skripsi', to='core.tugasakhir')),
                        ('ketua', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ketua_sidang', to='core.ketuasidang')),
                        ('penguji_utama', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='penguji_utama_sidang', to='core.dosen')),
                        ('pembimbing_utama', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pembimbing_utama_sidang', to='core.dosen')),
                        ('pembimbing_pendamping', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pembimbing_pendamping_sidang', to='core.dosen')),
                        ('notulis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notulis_sidang_staf', to='core.staf')),
                    ],
                    options={'db_table': 'layanan_akademik_sidangskripsi', 'verbose_name_plural': 'Jadwal Sidang Skripsi'},
                ),
                # JudulProposalSkripsi with OLD schema (single judul_proposal)
                # so Django knows the starting state before alteration
                migrations.CreateModel(
                    name='JudulProposalSkripsi',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('nim', models.CharField(max_length=20)),
                        ('nama_mahasiswa', models.CharField(max_length=100)),
                        ('program_studi', models.CharField(max_length=100)),
                        ('thn_akademik', models.CharField(max_length=50)),
                        ('judul_proposal', models.TextField()),
                        ('abstrak', models.TextField(blank=True)),
                        ('created_at', models.DateTimeField(auto_now_add=True)),
                    ],
                    options={'db_table': 'layanan_akademik_judulproposalskripsi', 'verbose_name_plural': 'Judul Proposal Skripsi', 'ordering': ['-created_at']},
                ),
            ],
            database_operations=[],  # Tables already exist, no DB changes needed
        ),
    ]

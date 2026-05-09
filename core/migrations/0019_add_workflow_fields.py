"""
Migration: Add workflow fields to JudulProposalSkripsi and TugasAkhir.
- JudulProposalSkripsi: status, judul_disetujui, pembimbing_utama, pembimbing_pendamping, catatan_tim
- TugasAkhir: metode_penelitian, rumusan_masalah, pembimbing_usulan
- Sync judul_proposal → judul_proposal1/2/3 (state only, DB already has these)
"""
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_register_layanan_akademik_models'),
    ]

    operations = [
        # --- Sync JudulProposalSkripsi state: judul_proposal → judul_proposal1/2/3 ---
        # DB already has judul_proposal1/2/3 columns (added earlier)
        # State still has old judul_proposal. Use SeparateDatabaseAndState to sync.
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(model_name='judulproposalskripsi', name='judul_proposal'),
                migrations.AddField(
                    model_name='judulproposalskripsi', name='judul_proposal1',
                    field=models.TextField(default='', verbose_name='Judul Proposal 1'),
                    preserve_default=False,
                ),
                migrations.AddField(
                    model_name='judulproposalskripsi', name='judul_proposal2',
                    field=models.TextField(default='', verbose_name='Judul Proposal 2'),
                    preserve_default=False,
                ),
                migrations.AddField(
                    model_name='judulproposalskripsi', name='judul_proposal3',
                    field=models.TextField(default='', verbose_name='Judul Proposal 3'),
                    preserve_default=False,
                ),
            ],
            database_operations=[],  # columns already exist in DB
        ),

        # --- Add NEW workflow fields to JudulProposalSkripsi ---
        migrations.AddField(
            model_name='judulproposalskripsi', name='status',
            field=models.CharField(choices=[
                ('pengajuan', 'Pengajuan (Menunggu Review)'),
                ('disetujui', 'Judul Disetujui'),
                ('bimbingan', 'Bimbingan Proposal'),
                ('seminar', 'Dijadwalkan Seminar'),
                ('lulus_seminar', 'Lulus Seminar Proposal'),
                ('skripsi', 'Terdaftar Tugas Akhir / Skripsi'),
                ('ditolak', 'Ditolak'),
            ], default='pengajuan', max_length=20),
        ),
        migrations.AddField(
            model_name='judulproposalskripsi', name='judul_disetujui',
            field=models.CharField(blank=True, choices=[
                ('', '-- Belum Dipilih --'),
                ('1', 'Judul Proposal 1'),
                ('2', 'Judul Proposal 2'),
                ('3', 'Judul Proposal 3'),
            ], default='', help_text='Pilih salah satu dari 3 judul yang diajukan',
               max_length=1, verbose_name='Judul yang Disetujui'),
        ),
        migrations.AddField(
            model_name='judulproposalskripsi', name='pembimbing_utama',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                     related_name='pembimbing_utama_proposal', to='core.dosen',
                                     verbose_name='Pembimbing Utama'),
        ),
        migrations.AddField(
            model_name='judulproposalskripsi', name='pembimbing_pendamping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                     related_name='pembimbing_pendamping_proposal', to='core.dosen',
                                     verbose_name='Pembimbing Pendamping'),
        ),
        migrations.AddField(
            model_name='judulproposalskripsi', name='catatan_tim',
            field=models.TextField(blank=True, verbose_name='Catatan Tim / Kaprodi'),
        ),

        # --- Add fields to TugasAkhir (columns may already exist in DB from phpMyAdmin) ---
        # Use SeparateDatabaseAndState - if columns exist, skip DB ops
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AddField(
                    model_name='tugasakhir', name='metode_penelitian',
                    field=models.TextField(blank=True, default='', verbose_name='Metode Penelitian'),
                ),
                migrations.AddField(
                    model_name='tugasakhir', name='rumusan_masalah',
                    field=models.TextField(blank=True, default='', verbose_name='Rumusan Masalah'),
                ),
                migrations.AddField(
                    model_name='tugasakhir', name='pembimbing_usulan',
                    field=models.CharField(blank=True, default='', max_length=200, verbose_name='Pembimbing Usulan'),
                ),
            ],
            database_operations=[],  # columns already exist in DB (added via phpMyAdmin)
        ),

        # --- Update Meta and field options ---
        migrations.AlterModelOptions(
            name='judulproposalskripsi',
            options={'ordering': ['-created_at'],
                     'verbose_name': 'Pengajuan Judul Proposal',
                     'verbose_name_plural': 'Pengajuan Judul Proposal Skripsi'},
        ),
        migrations.AlterModelOptions(
            name='seminarproposal',
            options={'verbose_name': 'Seminar Proposal',
                     'verbose_name_plural': 'Jadwal Seminar Proposal'},
        ),
        migrations.AlterField(
            model_name='seminarproposal', name='tugas_akhir',
            field=models.OneToOneField(
                help_text='Cari berdasarkan NIM atau nama mahasiswa',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='seminar_proposal',
                to='core.tugasakhir',
                verbose_name='Mahasiswa',
            ),
        ),
    ]

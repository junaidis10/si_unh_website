import os
import openpyxl
from django.core.management.base import BaseCommand
from core.models import SurveyKepuasanLulusan
from django.db import transaction

class Command(BaseCommand):
    help = 'Import survey data from Excel file using openpyxl'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
            return

        try:
            wb = openpyxl.load_workbook(file_path)
            ws = wb.active
            
            rows = list(ws.values)
            if not rows:
                self.stdout.write(self.style.WARNING('File is empty'))
                return
                
            headers = [str(h).lower().strip() for h in rows[0]]
            data_rows = rows[1:]
            
            def find_col_idx(keywords):
                for i, h in enumerate(headers):
                    if any(k in h for k in keywords):
                        return i
                return None

            col_idx = {
                'email': find_col_idx(['email', 'e-mail']),
                'nama_responden': find_col_idx(['nama responden', 'nama lengkap', 'nama']),
                'nama_instansi': find_col_idx(['nama instansi', 'perusahaan', 'nama perusahaan']),
                'jabatan': find_col_idx(['jabatan', 'posisi']),
                'integritas': find_col_idx(['integritas', 'etika', 'moral']),
                'keahlian_bidang': find_col_idx(['keahlian bidang', 'kompetensi utama', 'keahlian']),
                'bahasa_inggris': find_col_idx(['bahasa inggris', 'english']),
                'penggunaan_it': find_col_idx(['it', 'teknologi informasi']),
                'komunikasi': find_col_idx(['komunikasi']),
                'kerjasama_tim': find_col_idx(['kerjasama', 'tim', 'group']),
                'pengembangan_diri': find_col_idx(['pengembangan diri', 'belajar']),
                'waktu_tunggu': find_col_idx(['waktu tunggu', 'waiting time', 'wt']),
            }

            count = 0
            with transaction.atomic():
                for row in data_rows:
                    email = str(row[col_idx['email']]).strip() if col_idx['email'] is not None else None
                    if not email or SurveyKepuasanLulusan.objects.filter(email=email).exists():
                        continue

                    SurveyKepuasanLulusan.objects.create(
                        email=email,
                        nama_responden=str(row[col_idx['nama_responden']]) if col_idx['nama_responden'] is not None else '',
                        nama_instansi=str(row[col_idx['nama_instansi']]) if col_idx['nama_instansi'] is not None else '',
                        jabatan=str(row[col_idx['jabatan']]) if col_idx['jabatan'] is not None else 'Staff',
                        integritas=str(row[col_idx['integritas']]) if col_idx['integritas'] is not None else 'Baik',
                        keahlian_bidang=str(row[col_idx['keahlian_bidang']]) if col_idx['keahlian_bidang'] is not None else 'Baik',
                        bahasa_inggris=str(row[col_idx['bahasa_inggris']]) if col_idx['bahasa_inggris'] is not None else 'Baik',
                        penggunaan_it=str(row[col_idx['penggunaan_it']]) if col_idx['penggunaan_it'] is not None else 'Baik',
                        komunikasi=str(row[col_idx['komunikasi']]) if col_idx['komunikasi'] is not None else 'Baik',
                        kerjasama_tim=str(row[col_idx['kerjasama_tim']]) if col_idx['kerjasama_tim'] is not None else 'Baik',
                        pengembangan_diri=str(row[col_idx['pengembangan_diri']]) if col_idx['pengembangan_diri'] is not None else 'Baik',
                        waktu_tunggu=str(row[col_idx['waktu_tunggu']]) if col_idx['waktu_tunggu'] is not None else 'WT < 3',
                    )
                    count += 1

            self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} records'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))

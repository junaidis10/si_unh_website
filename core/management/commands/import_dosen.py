from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from core.models import Dosen
from django.core.files.base import ContentFile
import os
from urllib.parse import urljoin

class Command(BaseCommand):
    help = 'Scrape Dosen Tetap data from https://si.unh.ac.id/dosen'

    def handle(self, *args, **options):
        url = 'https://si.unh.ac.id/dosen'
        self.stdout.write(f'Fetching {url}...')
        
        try:
            response = requests.get(url, verify=False) # Skip SSL verify if needed, based on some unh sites
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching page: {e}'))
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all team members
        members = soup.select('.team-member')
        self.stdout.write(f'Found {len(members)} lecturers.')

        for member in members:
            try:
                # Basic Info
                info_div = member.select_one('.member-info')
                name = info_div.select_one('h4').text.strip()
                nidn_text = info_div.select_one('span').text.strip()
                nidn = nidn_text.replace('NIDN:', '').strip()
                
                self.stdout.write(f'Processing {name} ({nidn})...')

                # Photo
                img_tag = member.select_one('.member-img img')
                photo_url = urljoin(url, img_tag['src']) if img_tag else None

                # Find Modal for Details
                btn = info_div.select_one('button[data-target]')
                modal_id = btn['data-target'].replace('#', '') if btn else None
                
                email = ''
                bidang = ''
                sinta_link = ''

                if modal_id:
                    modal = soup.find(id=modal_id)
                    if modal:
                        # Email & Bidang
                        list_items = modal.select('.list-unstyled li')
                        for li in list_items:
                            text = li.text.strip()
                            if 'Email:' in text:
                                email = text.replace('Email:', '').strip()
                            elif 'Bidang Riset:' in text:
                                bidang = text.replace('Bidang Riset:', '').strip()
                        
                        # SINTA Link
                        sinta_btn = modal.select_one('a.btn-primary')
                        if sinta_btn:
                            sinta_link = sinta_btn['href']

                # Create or Update Dosen
                dosen, created = Dosen.objects.update_or_create(
                    nidn=nidn,
                    defaults={
                        'nama': name,
                        'kategori': 'tetap',
                        'email': email,
                        'bidang_keahlian': bidang,
                        'sinta_link': sinta_link,
                        'is_active': True
                    }
                )

                # Update Photo if exists
                if photo_url:
                    try:
                        img_response = requests.get(photo_url, verify=False)
                        if img_response.status_code == 200:
                            file_name = os.path.basename(photo_url)
                            dosen.photo.save(file_name, ContentFile(img_response.content), save=True)
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Failed to download photo for {name}: {e}'))

                action = "Created" if created else "Updated"
                self.stdout.write(self.style.SUCCESS(f'{action} {name}'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing member: {e}'))

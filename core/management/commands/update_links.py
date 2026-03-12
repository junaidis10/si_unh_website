from django.core.management.base import BaseCommand
from core.models import Dosen, Link

class Command(BaseCommand):
    help = 'Update content links for Dosen and Layanan'

    def handle(self, *args, **options):
        # 1. Update SINTA Links
        self.stdout.write("Updating SINTA links...")
        dosens = Dosen.objects.all()
        count = 0
        for dosen in dosens:
            if 'sinta.kemdikbud.go.id' in dosen.sinta_link:
                old_link = dosen.sinta_link
                new_link = old_link.replace('sinta.kemdikbud.go.id', 'sinta.kemdiktisaintek.go.id')
                dosen.sinta_link = new_link
                dosen.save()
                self.stdout.write(f"Updated {dosen.nama}: {old_link} -> {new_link}")
                count += 1
        self.stdout.write(self.style.SUCCESS(f"Updated {count} SINTA links."))

        # 2. Update Layanan Links
        self.stdout.write("Updating Layanan links...")
        
        # SIAKAD
        Link.objects.update_or_create(
            name='SIAKAD',
            defaults={
                'url': 'https://mhs.unh.ac.id',
                'kategori': 'siakad',
                'icon': 'fas fa-graduation-cap'
            }
        )
        self.stdout.write(self.style.SUCCESS("Updated SIAKAD link."))

        # OJS (Jurnal)
        Link.objects.update_or_create(
            name='Open Journal System',
            defaults={
                'url': 'https://ojs.unh.ac.id/',
                'kategori': 'ojs',
                'icon': 'fas fa-book'
            }
        )
        self.stdout.write(self.style.SUCCESS("Updated OJS link."))

        # Laboratorium RTIK (Check if exists first or create)
        # Search by name or URL part to be safe
        lab_link = Link.objects.filter(name__icontains='Laboratorium').first()
        if not lab_link:
            lab_link = Link(name='Laboratorium Komputer')
        
        lab_link.url = 'https://unh.ac.id/id/fasilitas/sarana-prasarana/laboratorium-komputer/laboratorium-komputer.html'
        lab_link.kategori = 'laboratorium'
        lab_link.icon = 'fas fa-desktop'
        lab_link.save()
        self.stdout.write(self.style.SUCCESS("Updated Laboratorium link."))

from django.core.management.base import BaseCommand
from core.models import Link

class Command(BaseCommand):
    help = 'Restore SIAKAD and Lab RTIK links'

    def handle(self, *args, **options):
        # Restore SIAKAD
        Link.objects.update_or_create(
            name='SIAKAD',
            defaults={
                'url': 'https://mhs.unh.ac.id',
                'kategori': 'siakad',
                'icon': 'fas fa-graduation-cap',
                'is_active': True
            }
        )
        self.stdout.write(self.style.SUCCESS("Restored SIAKAD link."))

        # Restore Laboratorium
        Link.objects.update_or_create(
            name='Laboratorium Komputer',
            defaults={
                'url': 'https://unh.ac.id/id/fasilitas/sarana-prasarana/laboratorium-komputer/laboratorium-komputer.html',
                'kategori': 'laboratorium',
                'icon': 'fas fa-desktop',
                'is_active': True
            }
        )
        self.stdout.write(self.style.SUCCESS("Restored Laboratorium link."))

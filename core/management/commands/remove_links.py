from django.core.management.base import BaseCommand
from core.models import Link

class Command(BaseCommand):
    help = 'Remove SIAKAD and Lab RTIK links'

    def handle(self, *args, **options):
        # Remove SIAKAD
        deleted_count, _ = Link.objects.filter(name__icontains='SIAKAD').delete()
        self.stdout.write(f"Deleted {deleted_count} SIAKAD links.")
        
        # Remove Lab RTIK (Laboratorium Komputer)
        deleted_count, _ = Link.objects.filter(name__icontains='Laboratorium').delete()
        self.stdout.write(f"Deleted {deleted_count} Laboratorium links.")

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from specialties.models import Specialty

class Command(BaseCommand):
    help = 'Seed database with specialty data'

    def handle(self, *args, **kwargs):
        titles = [
            'Cardiology',
            'Neurology',
            'Orthopedics',
            'Dermatology',
            'Gynecology',
            'Pediatrics'
        ]

        for title in titles:
            slug = slugify(title)
            obj, created = Specialty.objects.get_or_create(title=title, slug=slug, is_published=True)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Specialty {title} created'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Specialty {title} already exists'))

        self.stdout.write(self.style.SUCCESS('Specialties seeded successfully'))
import json
import os
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from location.models import Division, District, Thana


class Command(BaseCommand):
    help = 'Seed database with location data'

    def handle(self, *args, **kwargs):

        try:
            file_path = "data/divisions.json"
            with open(file_path, 'r', encoding='utf-8') as file:
                divisions = json.load(file)
                print(divisions)  # Optional: remove after testing

                for division in divisions:
                    obj, created = Division.objects.get_or_create(
                        name=division['name'],
                        slug=slugify(division['name']),
                        bn_name=division['bn_name']
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Division {division["name"]} created'))
                    else:
                        self.stdout.write(self.style.SUCCESS(f'Division {division["name"]} already exists'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'divisions.json not found at {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format in divisions.json'))
        except KeyError as e:
            self.stdout.write(self.style.ERROR(f'Missing key {e} in divisions.json'))

        
        try:
            file_path = "data/districts.json"
            with open(file_path, 'r', encoding='utf-8') as file:
                districts = json.load(file)
                for district in districts:
                    obj, created = District.objects.get_or_create(
                        name=district['name'], 
                        slug=slugify(district['name']), 
                        bn_name=district['bn_name'], 
                        division=Division.objects.get(id=district['division_id'])
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'District {district["name"]} created'))
                    else:
                        self.stdout.write(self.style.SUCCESS(f'District {district["name"]} already exists'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'districts.json not found at {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format in districts.json'))
        except KeyError as e:
            self.stdout.write(self.style.ERROR(f'Missing key {e} in districts.json'))


        try:
            file_path = "data/upazillas.json"
            with open(file_path, 'r', encoding='utf-8') as file:
                thanas = json.load(file)
                for thana in thanas:
                    print(thana)
                    district = District.objects.get(id=thana['district_id'])
                    division = Division.objects.get(id=district.division_id)
                    obj, created = Thana.objects.get_or_create(
                        name=thana['name'], 
                        slug=slugify(thana['name']), 
                        bn_name=thana['bn_name'], 
                        district=district, 
                        division=division
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Thana {thana["name"]} created'))
                    else:
                        self.stdout.write(self.style.SUCCESS(f'Thana {thana["name"]} already exists'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'upazillas.json not found at {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format in upazillas.json'))
        except KeyError as e:
            self.stdout.write(self.style.ERROR(f'Missing key {e} in upazillas.json'))

        self.stdout.write(self.style.SUCCESS('Locations seeded successfully'))
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from app.models import Location

class Command(BaseCommand):
    help = 'Adds sample location data to the database'

    def handle(self, *args, **options):
        # Delete all existing locations to avoid duplicates
        Location.objects.all().delete()
        
        # Sample locations with coordinates (longitude, latitude)
        sample_locations = [
            {
                'name': 'Eiffel Tower',
                'description': 'Iconic iron tower in Paris, France',
                'point': Point(2.2945, 48.8584)  # (longitude, latitude)
            },
            {
                'name': 'Statue of Liberty',
                'description': 'Famous statue in New York Harbor',
                'point': Point(-74.0445, 40.6892)
            },
            {
                'name': 'Sydney Opera House',
                'description': 'Performing arts center in Sydney, Australia',
                'point': Point(151.2153, -33.8568)
            },
            {
                'name': 'Taj Mahal',
                'description': 'Ivory-white marble mausoleum in Agra, India',
                'point': Point(78.0422, 27.1751)
            },
            {
                'name': 'Great Wall of China',
                'description': 'Ancient fortification in northern China',
                'point': Point(116.5704, 40.4319)
            }
        ]
        
        # Create location objects
        locations_created = 0
        for location_data in sample_locations:
            Location.objects.create(
                name=location_data['name'],
                description=location_data['description'],
                point=location_data['point']
            )
            locations_created += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully added {locations_created} sample locations')
        )
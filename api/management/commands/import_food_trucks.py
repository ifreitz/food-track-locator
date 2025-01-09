import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from api.models import FoodTruck

class Command(BaseCommand):
    help = 'Import food truck data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            trucks_created = 0
            
            for row in reader:
                try:
                    # Convert date strings to datetime objects
                    noi_sent = datetime.strptime(row['NOISent'], '%Y%m%d') if row['NOISent'] else None
                    approved = datetime.strptime(row['Approved'], '%Y%m%d') if row['Approved'] else None
                    received = datetime.strptime(row['Received'], '%Y%m%d')
                    expiration = datetime.strptime(row['ExpirationDate'], '%Y%m%d')

                    # Create FoodTruck instance
                    food_truck = FoodTruck(
                        location_id=int(row['locationid']),
                        applicant=row['Applicant'],
                        facility_type=row['FacilityType'],
                        cnn=int(row['cnn']),
                        location_description=row['LocationDescription'],
                        address=row['Address'],
                        block_lot=row['blocklot'],
                        block=row['block'],
                        lot=row['lot'],
                        permit=row['permit'],
                        status=row['Status'],
                        food_items=row['FoodItems'],
                        x_coordinate=float(row['X']),
                        y_coordinate=float(row['Y']),
                        latitude=float(row['Latitude']),
                        longitude=float(row['Longitude']),
                        schedule_url=row['Schedule'],
                        days_hours=row['dayshours'],
                        noi_sent=noi_sent,
                        approved_date=approved,
                        received_date=received,
                        prior_permit=bool(row['PriorPermit']),
                        expiration_date=expiration,
                        location=row['Location'],
                        fire_prevention_district=int(row['Fire Prevention Districts']),
                        police_district=int(row['Police Districts']),
                        supervisor_district=int(row['Supervisor Districts']),
                        zip_code=row['Zip Codes'],
                        neighborhood=int(row['Neighborhoods (old)'])
                    )
                    food_truck.save()
                    trucks_created += 1
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(
                            f'Error processing row {trucks_created + 1}: {str(e)}'
                        )
                    )
                    continue

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully imported {trucks_created} food trucks'
                )
            ) 
from django.db import models


class FoodTruck(models.Model):
    location_id = models.IntegerField(primary_key=True)
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=50)
    cnn = models.IntegerField()
    location_description = models.TextField()
    address = models.CharField(max_length=255)
    block_lot = models.CharField(max_length=20)
    block = models.CharField(max_length=10)
    lot = models.CharField(max_length=10)
    permit = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    food_items = models.TextField(null=True, blank=True)
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    schedule_url = models.URLField(max_length=500)
    days_hours = models.CharField(max_length=255, null=True, blank=True)
    noi_sent = models.DateTimeField(null=True, blank=True)
    approved_date = models.DateTimeField(null=True, blank=True)
    received_date = models.DateField()
    prior_permit = models.BooleanField()
    expiration_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    fire_prevention_district = models.IntegerField()
    police_district = models.IntegerField()
    supervisor_district = models.IntegerField()
    zip_code = models.CharField(max_length=10)
    neighborhood = models.IntegerField()

    def __str__(self):
        return f"{self.applicant} - {self.location_description}"

    class Meta:
        db_table = 'food_trucks'
        indexes = [
            models.Index(fields=['applicant']),
            models.Index(fields=['facility_type']),
            models.Index(fields=['status']),
            models.Index(fields=['latitude', 'longitude']),
        ]

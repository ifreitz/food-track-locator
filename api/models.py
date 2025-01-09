from django.db import models


class FoodTruck(models.Model):
    location_id = models.IntegerField(primary_key=True)
    applicant = models.CharField(max_length=255, null=True, blank=True)
    facility_type = models.CharField(max_length=50, null=True, blank=True)
    cnn = models.IntegerField(null=True, blank=True)
    location_description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    block_lot = models.CharField(max_length=20, null=True, blank=True)
    block = models.CharField(max_length=10, null=True, blank=True)
    lot = models.CharField(max_length=10, null=True, blank=True)
    permit = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    food_items = models.TextField(null=True, blank=True)
    x_coordinate = models.FloatField(null=True, blank=True)
    y_coordinate = models.FloatField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    schedule_url = models.URLField(max_length=500, null=True, blank=True)
    days_hours = models.CharField(max_length=255, null=True, blank=True)
    noi_sent = models.DateTimeField(null=True, blank=True)
    approved_date = models.DateTimeField(null=True, blank=True)
    received_date = models.DateField(null=True, blank=True)
    prior_permit = models.BooleanField(default=False)
    expiration_date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    fire_prevention_district = models.IntegerField(null=True, blank=True)
    police_district = models.IntegerField(null=True, blank=True)
    supervisor_district = models.IntegerField(null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    neighborhood = models.CharField(max_length=100, null=True, blank=True)

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

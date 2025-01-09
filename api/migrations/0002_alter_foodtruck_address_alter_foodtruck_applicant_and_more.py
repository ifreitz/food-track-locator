# Generated by Django 4.2.17 on 2025-01-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtruck',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='applicant',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='block',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='block_lot',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='cnn',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='facility_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='fire_prevention_district',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='location_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='lot',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='neighborhood',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='permit',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='police_district',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='prior_permit',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='received_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='schedule_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='supervisor_district',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='x_coordinate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='y_coordinate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
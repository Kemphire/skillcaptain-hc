# Generated by Django 5.0.6 on 2024-05-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='Adress of person <django.db.models.fields.CharField>', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_no',
            field=models.IntegerField(default=0),
        ),
    ]
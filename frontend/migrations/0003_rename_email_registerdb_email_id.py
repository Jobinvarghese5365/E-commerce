# Generated by Django 4.2.6 on 2023-12-12 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_registerdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerdb',
            old_name='email',
            new_name='email_id',
        ),
    ]
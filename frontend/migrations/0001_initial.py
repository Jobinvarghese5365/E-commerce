# Generated by Django 4.2.6 on 2023-12-08 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=50, null=True)),
                ('contact_subject', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_message', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
# Generated by Django 4.2.6 on 2023-12-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_alter_productdb_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='Category_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

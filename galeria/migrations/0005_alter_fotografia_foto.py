# Generated by Django 4.1.7 on 2023-04-08 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/'),
        ),
    ]

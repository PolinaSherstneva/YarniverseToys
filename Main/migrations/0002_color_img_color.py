# Generated by Django 4.2.5 on 2023-11-24 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='img_color',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]

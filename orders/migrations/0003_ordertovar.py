# Generated by Django 4.2.5 on 2023-11-23 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tovars', to='orders.order')),
                ('tovar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tovar_in_order', to='Main.tovar')),
            ],
        ),
    ]

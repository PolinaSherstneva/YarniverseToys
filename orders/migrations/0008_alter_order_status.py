# Generated by Django 4.2.5 on 2023-12-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Принят в работу', 'Принят в работу'), ('В сборке', 'В сборке'), ('В доставке', 'В доставке'), ('Выполнен', 'Выполнен')], default='Принят в работу', max_length=20),
        ),
    ]

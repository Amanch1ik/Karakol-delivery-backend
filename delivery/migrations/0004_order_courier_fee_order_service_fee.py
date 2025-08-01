# Generated by Django 5.2.3 on 2025-07-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_alter_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='courier_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Оплата курьеру', max_digits=8),
        ),
        migrations.AddField(
            model_name='order',
            name='service_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Комиссия сервиса', max_digits=8),
        ),
    ]

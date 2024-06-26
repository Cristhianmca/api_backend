# Generated by Django 4.2 on 2024-03-23 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_order_discount_order_total_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('account_email', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tbl_payment_method',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'pending'), ('2', 'complete')], default='1', max_length=1),
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('refer_number', models.TextField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.order')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.paymentmethod')),
            ],
            options={
                'db_table': 'tbl_order_payment',
            },
        ),
    ]

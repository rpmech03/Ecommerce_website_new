# Generated by Django 3.2.16 on 2023-01-02 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0010_orderplaced_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('alternate_mobile_number', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('business_name', models.CharField(max_length=200, unique=True)),
                ('shop_image', models.TextField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('shop_documents', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='vendor_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
    ]

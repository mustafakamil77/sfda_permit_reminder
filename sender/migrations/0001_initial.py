# Generated by Django 5.1.2 on 2024-11-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SdfaPermit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=200)),
                ('application_date', models.DateTimeField()),
                ('transaction_number', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_number', models.CharField(max_length=100, unique=True)),
                ('notes', models.CharField(blank=True, max_length=250, null=True)),
                ('release_date', models.DateTimeField(blank=True, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('renewal_date', models.DateTimeField(blank=True, null=True)),
                ('notify', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]

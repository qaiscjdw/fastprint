# Generated by Django 4.2.5 on 2023-10-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tes', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False)),
                ('nama_produk', models.CharField(blank=True, max_length=255, null=True)),
                ('harga', models.IntegerField(blank=True, null=True)),
                ('kategori_id', models.IntegerField(blank=True, null=True)),
                ('status_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'produk',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id_status', models.AutoField(primary_key=True, serialize=False)),
                ('nama_status', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'status',
                'managed': True,
            },
        ),
    ]

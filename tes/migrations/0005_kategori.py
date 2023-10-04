# Generated by Django 4.2.5 on 2023-10-03 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tes', '0004_produk_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'kategori',
                'managed': True,
            },
        ),
    ]
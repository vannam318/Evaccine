# Generated by Django 4.1.7 on 2023-05-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0011_relative'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vaccineinfo',
            options={'ordering': ['Tên_Vaccine']},
        ),
        migrations.AddField(
            model_name='vaccineinfo',
            name='Ghi_chú',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='vaccineinfo',
            name='Liều_lượng',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='vaccineinfo',
            name='Sức_khỏe_sau_khi_tiêm',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='vaccineinfo',
            name='Sức_khỏe_trước_khi_tiêm',
            field=models.TextField(blank=True),
        ),
    ]

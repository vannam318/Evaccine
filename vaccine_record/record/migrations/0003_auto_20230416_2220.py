# Generated by Django 4.1.7 on 2023-04-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20230416_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='Ngày_tiêm',
            field=models.DateField(blank=True, null=True, help_text='Date'),
        ),
    ]
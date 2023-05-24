# Generated by Django 4.1.7 on 2023-05-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0012_alter_vaccineinfo_options_vaccineinfo_ghi_chú_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relative',
            name='Relative_name',
            field=models.CharField(help_text='Họ và tên', max_length=200),
        ),
        migrations.AlterField(
            model_name='relative',
            name='Role',
            field=models.CharField(help_text='Quan hệ', max_length=200),
        ),
        migrations.AlterField(
            model_name='relative',
            name='Tuoi',
            field=models.IntegerField(blank=True, help_text='Tuổi', null=True),
        ),
    ]
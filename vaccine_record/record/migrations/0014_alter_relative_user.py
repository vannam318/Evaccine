# Generated by Django 4.1.7 on 2023-05-21 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('record', '0013_alter_relative_relative_name_alter_relative_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relative',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

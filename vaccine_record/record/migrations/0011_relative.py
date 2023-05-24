# Generated by Django 4.1.7 on 2023-05-21 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0010_alter_vaccineinfo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.CharField(help_text='ba,mẹ,anh,chị,em,...', max_length=254)),
                ('Relative_name', models.CharField(default='', max_length=254)),
                ('Tuoi', models.IntegerField()),
                ('Ngày_sinh', models.DateField(blank=True, help_text='(vd: 2002-08-31)', null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='record.user')),
            ],
        ),
    ]

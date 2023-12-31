# Generated by Django 4.1 on 2023-06-15 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_file', models.CharField(blank=True, max_length=255)),
                ('main_file', models.FileField(upload_to='data_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('total_downloads', models.IntegerField()),
            ],
        ),
    ]

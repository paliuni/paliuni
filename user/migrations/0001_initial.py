# Generated by Django 3.1.3 on 2020-12-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=12)),
                ('message', models.TextField()),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
    ]

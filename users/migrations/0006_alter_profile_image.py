# Generated by Django 3.2.6 on 2021-08-15 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg.jpg', upload_to='profile_pics'),
        ),
    ]
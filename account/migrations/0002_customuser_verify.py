# Generated by Django 3.1 on 2020-09-11 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verify',
            field=models.BooleanField(default=False),
        ),
    ]

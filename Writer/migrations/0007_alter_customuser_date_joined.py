# Generated by Django 4.0.5 on 2022-06-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Writer', '0006_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

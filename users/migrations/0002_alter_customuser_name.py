# Generated by Django 4.2.7 on 2023-12-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='memory',
            field=models.CharField(max_length=100),
        ),
    ]
# Generated by Django 3.1 on 2020-09-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstaap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productentry',
            name='productdesc',
            field=models.TextField(max_length=100),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_personal_vehiculos'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='puesto',
            field=models.CharField(max_length=100, null=b'I01\n'),
            preserve_default=b'I01\n',
        ),
    ]

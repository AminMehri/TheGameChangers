# Generated by Django 2.2 on 2021-11-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(upload_to='images'),
        ),
    ]

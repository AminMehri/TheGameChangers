# Generated by Django 2.2 on 2021-12-01 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20211118_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_author',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_name',
            field=models.CharField(default=None, max_length=255),
        ),
    ]

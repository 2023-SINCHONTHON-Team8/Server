# Generated by Django 4.2.4 on 2023-08-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta_vibes', models.BooleanField(default=False)),
                ('local_legend', models.BooleanField(default=False)),
                ('trending_spot', models.BooleanField(default=False)),
                ('secret_spot', models.BooleanField(default=False)),
                ('mint_choco', models.BooleanField(default=False)),
                ('perilla_leaves', models.BooleanField(default=False)),
                ('mara', models.BooleanField(default=False)),
                ('hawaiian_pizza', models.BooleanField(default=False)),
                ('cucumber', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Likes',
            },
        ),
        migrations.AlterModelManagers(
            name='member',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='spicy',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
    ]
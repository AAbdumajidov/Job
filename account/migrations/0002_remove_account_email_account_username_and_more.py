# Generated by Django 4.2 on 2023-05-05 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(db_index=True, default=-0.1, max_length=221, unique=True, verbose_name='Username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.IntegerField(choices=[(0, 'HR'), (1, 'Candidate'), (2, 'Stuff')], default=2),
        ),
    ]

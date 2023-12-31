# Generated by Django 4.2 on 2023-05-05 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_account_email_account_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(db_index=True, default=-0.1, max_length=50, unique=True, verbose_name='Email'),
            preserve_default=False,
        ),
    ]

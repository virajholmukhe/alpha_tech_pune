# Generated by Django 3.2.4 on 2021-07-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_emailusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailusers',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
    ]

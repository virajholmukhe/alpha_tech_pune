# Generated by Django 3.2.4 on 2021-07-15 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0002_auto_20210715_0715'),
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.userinfo')),
            ],
            options={
                'db_table': 'MyCart',
            },
        ),
    ]

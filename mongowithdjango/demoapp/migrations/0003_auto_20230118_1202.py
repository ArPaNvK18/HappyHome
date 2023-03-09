# Generated by Django 3.2.6 on 2023-01-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_expence'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyExpence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('date', models.DateField(max_length=10)),
                ('prise', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Expence',
        ),
    ]
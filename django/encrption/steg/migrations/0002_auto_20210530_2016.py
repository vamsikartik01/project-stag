# Generated by Django 3.0.6 on 2021-05-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Secure', 'Secure'), ('Unsecure', 'Unsecure')], max_length=10, null=True),
        ),
    ]

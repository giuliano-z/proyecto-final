# Generated by Django 4.2.3 on 2023-07-14 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-15 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_remove_libro_foto_libro_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
    ]
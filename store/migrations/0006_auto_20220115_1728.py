# Generated by Django 3.1 on 2022-01-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('size', 'size')], max_length=100),
        ),
    ]

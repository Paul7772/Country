# Generated by Django 5.0.4 on 2024-04-25 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infocountry', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name']},
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['name'], name='infocountry_name_b292fd_idx'),
        ),
    ]
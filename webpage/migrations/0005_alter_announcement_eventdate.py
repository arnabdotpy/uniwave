# Generated by Django 4.2.6 on 2023-11-15 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_rename_date_announcement_eventdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='eventDate',
            field=models.DateField(),
        ),
    ]
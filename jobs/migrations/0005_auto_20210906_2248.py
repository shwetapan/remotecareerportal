# Generated by Django 3.0 on 2021-09-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20210906_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='date_posted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
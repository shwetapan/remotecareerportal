# Generated by Django 3.0 on 2021-09-06 09:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20210904_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='type',
            new_name='job_type',
        ),
        migrations.AddField(
            model_name='jobs',
            name='company_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='is_closed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='is_published',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='last_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='salary',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

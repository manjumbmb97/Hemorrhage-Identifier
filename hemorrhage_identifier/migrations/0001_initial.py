# Generated by Django 2.1.3 on 2018-11-07 06:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hemorrhage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ct_scan_image', models.FileField(help_text='upload jpg, jpeg, png files only', null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])])),
                ('output', models.IntegerField(default=0)),
                ('is_output_correct', models.BooleanField(default=False)),
            ],
        ),
    ]

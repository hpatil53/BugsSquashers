# Generated by Django 3.0.8 on 2020-07-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_child_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child_details',
            old_name='c_catagory',
            new_name='c_category',
        ),
        migrations.AlterField(
            model_name='child_details',
            name='c_mobile_num',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]

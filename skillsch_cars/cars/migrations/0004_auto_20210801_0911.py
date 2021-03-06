# Generated by Django 3.2.5 on 2021-08-01 09:11

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20210730_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('3', '3'), ('6', '6'), ('5', '5'), ('2', '2'), ('4', '4')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('first_features', 'first_features'), ('second_features', 'second_features'), ('third_features', 'third_features'), ('fourth_features', 'fourth_features')], max_length=61),
        ),
    ]

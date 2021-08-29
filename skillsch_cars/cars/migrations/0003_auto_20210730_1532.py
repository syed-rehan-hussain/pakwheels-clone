# Generated by Django 3.2.5 on 2021-07-30 15:32

import ckeditor.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20210730_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('5', '5'), ('2', '2'), ('6', '6'), ('3', '3'), ('4', '4')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'first_features'), ('2', 'second_features'), ('3', 'third_features'), ('4', 'fourth_features')], max_length=7),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], verbose_name='year'),
        ),
    ]
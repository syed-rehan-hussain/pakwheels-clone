from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):
    state_choice = (
        ('SD','Sindh'),
        ('KPK','Pakthunkhwa'),
        ('ISB','Islamabad'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    doors_choice = {
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    }

    features_choice = (
        ('first_features', 'first_features'),
        ('second_features', 'second_features'),
        ('third_features', 'third_features'),
        ('fourth_features', 'fourth_features'),
    )


    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=255)
    price = models.IntegerField()
    description = RichTextField()
    carphoto = models.ImageField(upload_to='photos/%y/%m/%d/')
    carphoto1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    carphoto2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    carphoto3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    carphoto4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choice)
    body_style = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    interior = models.CharField(max_length=255)
    miles = models.IntegerField()
    doors = models.CharField(choices=doors_choice, max_length=100)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=255)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=255)
    no_of_owners = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now , blank=True)

    def __str__(self):
        return self.car_title
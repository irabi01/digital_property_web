from django.db import models

# Create your models here.
class Land(models.Model):
    location = (
        ('Arusha','Arusha'),('Dar es salaam','Dar es salaam'),('Dodoma','Dodoma'),('Morogoro','Morogoro'),
        ('Bukoba','Bukoba'),('Moshi','Moshi'),('Kilimanjaro','Kilimanjaro'),('Singida','Singida'),('Tabora','Tabora'),
        ('Tanga','Tanga'),('Iringa','Iringa'),('Songea','Songea'),('Mbeya','Mbeya'),('Mtwara','Mtwara'),
        ('Ruvuma','Ruvuma'),('Kigoma','Kigoma'),('Mombasa','Mombasa'),('Mwanza','Mwanza'),('Babati','Babati'),
        ('Sumbawanga','Sumbawanga')
    )
    Title = models.CharField(max_length = 50)
    Location = models.CharField(max_length = 50, choices = location)
    Area = models.CharField(max_length = 50)
    Image = models.CharField(max_length = 200)
    Price = models.CharField(max_length = 20)
    Description = models.TextField()
    class Meta:
        verbose_name_plural = "Land Property"
    def __str__(self):
        return self.Title +' - '+ self.Location

class House(models.Model):
    location = (
        ('Arusha','Arusha'),('Dar es salaam','Dar es salaam'),('Dodoma','Dodoma'),('Morogoro','Morogoro'),
        ('Bukoba','Bukoba'),('Moshi','Moshi'),('Kilimanjaro','Kilimanjaro'),('Singida','Singida'),('Tabora','Tabora'),
        ('Tanga','Tanga'),('Iringa','Iringa'),('Songea','Songea'),('Mbeya','Mbeya'),('Mtwara','Mtwara'),
        ('Ruvuma','Ruvuma'),('Kigoma','Kigoma'),('Mombasa','Mombasa'),('Mwanza','Mwanza'),('Babati','Babati'),
        ('Sumbawanga','Sumbawanga')
    )
    type = (
        ('For rent','For rent'),('For sell','For sell')
    )
    bedrooms = (
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')
    )
    Title = models.CharField(max_length = 50)
    Location = models.CharField(max_length = 50, choices = location)
    Type = models.CharField(max_length = 50, choices = type)
    Number_of_bedrooms = models.CharField(max_length = 50, choices = bedrooms)
    Image = models.CharField(max_length = 200)
    Price = models.CharField(max_length = 20)
    Description = models.TextField()
    class Meta:
        verbose_name_plural = "House Property"
    def __str__(self):
        return self.Title +' - '+ self.Location

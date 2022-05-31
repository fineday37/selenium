from django.db import models


# Create your models here.
class Test(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.CharField(max_length=32)
    pub_date = models.DateField()


class Emp(models.Model):
    objects = None

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    wage = models.FloatField(max_length=8, default=2)

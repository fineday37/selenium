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
    title = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    pub_date = models.DateField()
    test_id = models.ForeignKey("Test", on_delete=models.CASCADE)
    authors = models.ManyToManyField("Emp")


class Emp(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    wage = models.FloatField(max_length=8, default=2)


class Personnel(models.Model):
    object = None
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    salary = models.IntegerField()

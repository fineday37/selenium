from django.contrib import admin
from .models import Test, Contact, Tag, Book

# Register your models here.
admin.site.register([Test, Contact, Tag, Book])

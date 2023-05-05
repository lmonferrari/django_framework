from django.db import models


class Document(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(
        upload_to='clients_photos', null=True, blank=True)

    doc = models.OneToOneField(
        Document, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name


class Product(models.Model):
    number = models.CharField(max_length=7)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    product = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.product


class Sale(models.Model):
    number = models.CharField(max_length=7)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)

    person = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.PROTECT)

    products = models.ManyToManyField(Product, blank=True)

    def __str__(self) -> str:
        return self.number

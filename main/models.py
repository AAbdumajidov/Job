from django.db import models


class Type(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=221)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Position(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


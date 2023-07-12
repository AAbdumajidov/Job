from django.db import models
from blog.models import Category
from account.models import Account
from main.models import Type, City, Company


class Job(models.Model):
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=221)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(decimal_places=3, max_digits=4, null=True, blank=True)
    working_day = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    job = models.OneToOneField(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class Rezume(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    rezume = models.FileField()

    def __str__(self):
        return self.author



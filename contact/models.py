from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Subscribe(models.Model):
    email = models.EmailField()

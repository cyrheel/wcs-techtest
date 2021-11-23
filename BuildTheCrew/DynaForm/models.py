"""
1) Change your models (in models.py).
2) Run python manage.py makemigrations to create migrations for those changes
3) Run python manage.py migrate to apply those changes to the database.
"""
from django.db import models


class Argonaute(models.Model):
    argo_name = models.CharField(max_length=64)
    add_date = models.DateTimeField("Date added")

    def __str__(self):
        return self.argo_name

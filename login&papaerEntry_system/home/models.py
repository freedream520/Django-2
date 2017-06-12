# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    number = models.TextField(primary_key=True)
    username = models.TextField()
    sex = models.TextField()
    age = models.TextField()
    department = models.TextField()
    jobTitle = models.TextField()
    password = models.TextField()


class Paper(models.Model):
    paperTitle = models.TextField(primary_key=True)
    journalName = models.TextField()
    papaerDate = models.DateTimeField()
    papaerAuthor = models.TextField()
    uploadedBy = models.TextField()

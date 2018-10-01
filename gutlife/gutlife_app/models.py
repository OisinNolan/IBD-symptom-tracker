# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class BMLog(models.Model):
    consistency = models.IntegerField()
    solidity = models.IntegerField()
    datecode = models.DateField()
    time = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
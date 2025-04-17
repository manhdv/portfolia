# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stocks')
    ticker = models.CharField(max_length=10)
    exchange = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100, blank=True)
    sector = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, default='Vietnam')
    is_active = models.BooleanField(default=True)

    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    class Meta:
        unique_together = ('user', 'ticker')
    def __str__(self):
        return f"{self.ticker} - {self.name}"
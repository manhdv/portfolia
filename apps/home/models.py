# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Tham chiếu đến User
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    about_me = models.TextField()

    finhub_api_key = models.CharField(max_length=255, blank=True, null=True)
    alpha_vantage_api_key = models.CharField(max_length=255, blank=True, null=True)
    eodhd_api_key = models.CharField(max_length=255, blank=True, null=True)
    yahoo_finance_api_key = models.CharField(max_length=255, blank=True, null=True)
    google_map_api_key = models.CharField(max_length=255, blank=True, null=True)

    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
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
        indexes = [
            models.Index(fields=['user', 'ticker']),
        ]
    def __str__(self):
        return f"{self.ticker} - {self.name}"


class StockPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    date = models.DateField()
    close = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('stock', 'date')

    def __str__(self):
        return f"{self.stock.ticker} - {self.date} - {self.close}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Tham chiếu đến User
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    about_me = models.TextField()

    finhub_api_key = models.CharField(max_length=255, blank=True, null=True)
    alpha_vantage_api_key = models.CharField(max_length=255, blank=True, null=True)
    stock_source_1_api_key = models.CharField(max_length=255, blank=True, null=True)
    stock_source_2_api_key = models.CharField(max_length=255, blank=True, null=True)
    stock_source_3_api_key = models.CharField(max_length=255, blank=True, null=True)

    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username
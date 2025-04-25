# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Securities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='securities')
    code = models.CharField(max_length=10)
    exchange = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True)  
    country = models.CharField(max_length=50, default='VN')
    currency = models.CharField(max_length=50, default='VND')
    isin = models.CharField(max_length=20, blank=True)
    close = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    date = models.DateField(default=date.today)
    is_active = models.BooleanField(default=True)

    # metadata
    industry = models.CharField(max_length=100, blank=True)
    sector = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'code'], name='unique_user_code')
        ]
        indexes = [
            models.Index(fields=['user', 'code']),
        ]
    def __str__(self):
        return f"{self.code} - {self.name}"


class SecuritiesPrice(models.Model):
    securities = models.ForeignKey(Securities, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    open = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    high = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    low = models.DecimalField(max_digits=16, decimal_places=2,default=0)
    close = models.DecimalField(max_digits=16, decimal_places=2)
    adjusted_close = models.DecimalField(max_digits=16, decimal_places=2,default=0)
    volume = models.BigIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['securities', 'date'], name='unique_securities_date')
        ]
    def __str__(self):
        return f"{self.securities.code} - {self.date} - {self.close}"

from django.db import models
from django.contrib.auth.models import User

class RequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    ip_address=models.CharField(max_length=50)
    endpoint=models.CharField(max_length=200)
    method=models.CharField(max_length=10)
    status_code=models.IntegerField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} -{self.endpoint} "

from django.db import models

class BlockedIP(models.Model):
    ip_address = models.CharField(max_length=50, unique=True)
    reason = models.CharField(max_length=100)
    violation_count = models.IntegerField(default=0)
    last_violation_time = models.DateTimeField(null=True, blank=True)
    blocked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address
class WhitelistedIP(models.Model):
    ip_address=models.CharField(
        max_length=50,
        unique=True
    )
    reason=models.CharField(
        max_length=100,
        blank=True,
    )
    def __str__(self):
        return self.ip_address

class FailedLogin(models.Model):
    username=models.CharField(max_length=100)
    ip_address=models.CharField(max_length=50)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
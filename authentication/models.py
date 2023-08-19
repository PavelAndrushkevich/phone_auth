from django.db import models

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    invite_code = models.CharField(max_length=10, unique=True, null=True)
    is_authenticated = models.BooleanField(default=False)
    activated_invite_code = models.CharField(max_length=10, null=True, blank=True)
class AuthCode(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    code = models.CharField(max_length=4)



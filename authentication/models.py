from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.db import models

# Create your models here.


class CustomUser(models.Model):
    username = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    token = models.CharField(max_length=200, null=True, blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        # Hash the password before saving
        self.password = make_password(self.password)
        super(CustomUser, self).save(force_insert, force_update, using, update_fields)

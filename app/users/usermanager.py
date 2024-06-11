from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.db.models import Q


class MyUserManagers(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The ID must be set")
        if not password:
            raise ValueError("The Password must set")
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.setdefault("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        # is_superuser
        if extra_fields.setdefault("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
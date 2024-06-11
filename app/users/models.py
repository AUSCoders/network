from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .usermanager  import (
    MyUserManagers,
)
from django.core.validators import RegexValidator

id_regex = RegexValidator(regex=r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', message="Please enter valid Email address.")
# string_regex =  RegexValidator(regex=r'^[a-zA-Z]+(?:\s[a-zA-Z]+)*$', message="Some special characters like (~!#^`'$|{}<>*) are not allowed.")
# mobile_validate = RegexValidator(regex=r'^(\+\d{1,3})?\d{10}$',message='Enter a valid 10-digit mobile number +998 XX XXX XX XX')

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, db_index=True, validators=[id_regex])
    username = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    updated=models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)
    
    objects = MyUserManagers()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return str(self.email)

    def has_perm(self, perm, obj=None) -> bool:
        return self.is_staff

    def has_module_perms(self, app_label) -> bool:
        return True

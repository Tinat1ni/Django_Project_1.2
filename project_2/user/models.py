from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.db import models


class UserManager(BaseUserManager):
     def create_user(self, username, password=None, **extra_fields):
         if not username:
             raise ValueError('username iis required')
         if not password:
             raise ValueError('password is required')

         email = extra_fields.get('email')
         if email:
             email = self.normalize_email(email)

         user = self.model(username=username, email=email, **extra_fields)
         user.set_password(password)
         user.save(using=self._db)
         return user


     def create_superuser(self, username, email, password=None, **extra_fields):
         if not email:
             raise ValueError('Email is required')
         if not password:
             raise ValueError('password is required')

         extra_fields.setdefault('is_superuser', True)
         extra_fields.setdefault('is_active', True)
         extra_fields.setdefault('is_staff', True)

         user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
         user.set_password(password)
         user.save(using=self._db)
         return user


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

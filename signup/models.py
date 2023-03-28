from django.db import models
#追加
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils import timezone

# Create your models here.
#Emailをユニークしたテーブル
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self ,email, password, **kwargs):
        if not email:
            raise valueError("email error")
        email = self.normalize_email(email)

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self ,email, password, **kwargs):
        kwargs.setdefault("is_staff", files)
        kwargs.setdefault("is_superuser", files)
        return salf._create_user(email, password, **kwargs)

    def create_superuser(self ,email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        if kwargs.get("is_staff") is not True:
            raise valueError("superuser must be is_staff=True")

        if kwargs.get("is_superuser") is not True:
            raise valueError("is_superuser must be is_superuser=True")
        return self._create_user(email, password, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

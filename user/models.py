from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
# Create your models here.
# from datetime import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    use_in_migrations = True 

    def _create_user_object(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)

        user = self.model(email=email)
        user.password = make_password(password)
        return user 

    def _create_user(self, email, password, **extra_fields):
        """
        create and save user with email and password only
        """
        user = self._create_user_object(email, password, **extra_fields)
        user.save(using=self._db)
        return user 

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email=email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    This user model implements fully featured permission
    """

    email = models.EmailField(_("email address"), max_length=200, unique=True, blank=False)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
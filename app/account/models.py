from statistics import mode
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.conf import settings


from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)
    first_name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('Фамилия', max_length=50)
    third_name = models.CharField('Отчество', max_length=50)
    USERNAME_FIELD = "email" # make the user log in with the email
    REQUIRED_FIELDS = []

    objects = UserManager()



class SkillTag(models.Model):
    tag_name = models.CharField(max_length = 50)
    
    def __str__ (self):
        return self.tag_name
class Skill(models.Model):
    user = models.ManyToManyField(CustomUser, related_name='related_skills', blank=False)
    tag = models.ForeignKey(SkillTag, max_length = 50, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length = 50)
    
    def __str__ (self):
        return self.skill_name



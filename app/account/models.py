from statistics import mode
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)
    first_name = models.CharField('first_name', max_length=50)
    second_name = models.CharField('second_name', max_length=50)
    third_name = models.CharField('third_name', max_length=50)
    USERNAME_FIELD = "email" # make the user log in with the email
    REQUIRED_FIELDS = []



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



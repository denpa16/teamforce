# Generated by Django 4.0.4 on 2022-05-20 12:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_skill_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='user',
            field=models.ManyToManyField(related_name='related_skills', to=settings.AUTH_USER_MODEL),
        ),
    ]

from dataclasses import field
from logging import PlaceHolder
from pyexpat import model
from statistics import mode
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelChoiceField
from .models import CustomUser, Skill, SkillTag

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'second_name', 'third_name',)

class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput,  label='Пароль')


"""class SkillTagChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.get_tag()

class SkillNameChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.get_name()
"""

class SkillForm(forms.Form):
    tag = forms.ModelChoiceField(queryset=SkillTag.objects.all(), to_field_name='tag_name', label='Тэг')
    skill = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), to_field_name='skill_name', label='Навык')

class CustomSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['tag', 'skill_name']
        widgets = {
            'tag':forms.TextInput(attrs={'placeholder': 'Введите тэг'}),
            'skill_name':forms.TextInput(attrs={'placeholder': 'Введите навык'})
        }
    


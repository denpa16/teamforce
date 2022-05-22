from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .models import CustomUser, Skill, SkillTag
from .forms import SkillForm, CustomSkillForm
from .models import CustomUser
from .forms import SignUpForm, LogInForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account:home')
    else:
        form = SignUpForm()   
    return render(request, 'account/signup.html', {'form': form})


def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)  
                return redirect('account:home')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'account/login.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect(reverse('account:login'))

@login_required
def home(request):
    customusers = CustomUser.objects.all()
    skills = Skill.objects.all()
    skill_form = SkillForm()
    print(customusers)
    #print(users[1].id)
    #print(users[1].related_skills.count())
    #specuser = CustomUser.objects.get(id=9)
    #print(user.related_skills.all())
    return render(request, 'account/home.html', {'skills': skills, 'skill_form': skill_form, 'customusers': customusers,})

@login_required
def add_skill(request):
    skills = Skill.objects.all()
    skill_form = SkillForm()
    customskill_form = CustomSkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.skill = form.cleaned_data['skill']
            for skill in form.skill:
                request.user.related_skills.add(skill)
                print(skill)
            print(request.user.related_skills.all())
    return render(request, 'account/addskill.html', {'customskill_form': customskill_form, 'skill_form': skill_form,'skills': skills,})

@login_required
def add_customskill(request):
    if request.method == "POST":
        try:
            tag = SkillTag.objects.get(tag_name = request.POST['tag'])
        except:
            tag = SkillTag()
            tag.tag_name = request.POST['tag'].capitalize()
            tag.save()
        try:
            skill = Skill.objects.get(skill_name = request.POST['skill_name'])
            if skill not in request.user.related_skills.all():
                skill.user.add(request.user)
        except:
            skill = Skill()
            skill.skill_name = request.POST['skill_name'].capitalize()
            skill.tag = tag
            skill.save()
            skill.user.add(request.user)
    return redirect(reverse('account:add_skill'))


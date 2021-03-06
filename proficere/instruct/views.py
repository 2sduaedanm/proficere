from django.shortcuts import render, redirect 
from django.http import HttpResponse
#from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'instruct/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'instruct/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):

	context = {}

	return render(request, 'instruct/dashboard.html', context)


@login_required(login_url='login')
def instructor_home(request):

	context = {}

	return render(request, 'instruct/dashboard.html', context)


@login_required(login_url='login')
def student_home(request):

	pastProgressions = StudentCurriculum.objects.filter(studentid= request.user, statusid = 3)
	currentProgressions = StudentCurriculum.objects.filter(studentid= request.user, statusid__in = [1,2])
	context = {"pastProgressions":pastProgressions,"currentProgressions":currentProgressions}

	return render(request, 'instruct/studentHome.html', context)

@login_required(login_url='login')
def display_curriculum_challenges(request,curriculumid):

	challengeList = ChallengeCurriculum.objects.filter(curriculumid= curriculumid)
	curriculum = Curriculum.objects.get(id=curriculumid)
	context = {"curriculum":curriculum, "challengeList":challengeList}

	return render(request, 'instruct/CurriculumOverview.html', context)

@login_required(login_url='login')
def display_progression_curriculums(request,progressionid):

	curriculumList = Curriculum.objects.filter(progressionid= progressionid)
	context = {"curriculumList":curriculumList}

	return render(request, 'instruct/ProgressionOverview.html', context)


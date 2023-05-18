from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .utils import render_to_pdf

from .models import Experience, Education, Skill
from user_profile.models import UserProfile


def home(request):
	return render(request, '/home/dzee/resume_builder/index.html')

def profile(request):
	user = request.user
	profile = get_object_or_404(UserProfile, user=user)
	context = {
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
		'phone': profile.phone,
		'profession': profile.profession,
		'bio': profile.bio,
		'theme': profile.color,
	}
	return render(request, 'resume/profile.html', context)

def update_user(request):
	user = request.user
	user.first_name = request.POST['first_name']
	user.last_name = request.POST['last_name']
	user.email = request.POST['email']
	user.save()
	profile = get_object_or_404(UserProfile, user=user)
	profile.phone = request.POST['phone']
	profile.profession = request.POST['profession']
	profile.bio = request.POST['bio']
	profile.save()
	return HttpResponseRedirect(reverse('resume:profile'))

################################# CRUD EXPERIENCE

def experience(request):
	user = request.user
	profile = get_object_or_404(UserProfile, user=user)
	experiences = Experience.objects.filter(user=request.user)
	if experience:
		context = {
			'experiences': experiences,
			'theme': profile.color,
		}
		return render(request, 'resume/experience.html', context)
	context = {
		'theme': profile.color,
	}
	return render(request, 'resume/experience.html', context)

def create_experience(request):
	experience = Experience()
	experience.user = request.user
	experience.company = request.POST['company']
	experience.role = request.POST['role']
	experience.startDate = request.POST['start']
	experience.endDate = request.POST['end']
	experience.description = request.POST['description']
	experience.save()
	return HttpResponseRedirect(reverse('resume:experience'))

def update_experience(request):
	id = request.POST['id']
	experience =get_object_or_404(Experience, id=id)
	experience.company = request.POST['company']
	experience.role = request.POST['role']
	# experience.startDate = request.POST['start']
	# experience.endDate = request.POST['end']
	experience.description = request.POST['description']
	experience.save()
	return HttpResponseRedirect(reverse('resume:experience'))

def delete_experience(request, id):
	experience = get_object_or_404(Experience, id=id)
	experience.delete()
	return HttpResponseRedirect(reverse('resume:experience'))

################################# CRUD EDUCAION 

def education(request):
	user = request.user
	profile = get_object_or_404(UserProfile, user=user)
	educations = Education.objects.filter(user=request.user)
	if educations:
		context = {
			'educations': educations,
			'theme': profile.color,
		}
		return render(request, 'resume/education.html', context)
	context = {
		'theme': profile.color,
	}
	return render(request, 'resume/education.html', context)

def create_education(request):
	education = Education()
	education.user = request.user
	education.school = request.POST['school']
	education.degree = request.POST['degree']
	education.startDate = request.POST['start']
	education.endDate = request.POST['end']
	education.description = request.POST['description']
	education.save()
	return HttpResponseRedirect(reverse('resume:education'))

def update_education(request):
	id = request.POST['id']
	education =get_object_or_404(Education, id=id)
	education.school = request.POST['school']
	education.degree = request.POST['degree']
	# education.startDate = request.POST['start']
	# education.endDate = request.POST['end']
	education.description = request.POST['description']
	education.save()
	return HttpResponseRedirect(reverse('resume:education'))

def delete_education(request, id):
	education = get_object_or_404(Education, id=id)
	education.delete()
	return HttpResponseRedirect(reverse('resume:education'))


################################# CRUD SKILL

def skills(request):
	user = request.user
	profile = get_object_or_404(UserProfile, user=user)
	skills = Skill.objects.filter(user=request.user)
	skills = skills[::-1] ##reversing the list
	context = {
		'skills': skills,
		'theme': profile.color,
	}
	return render(request, 'resume/skills.html', context)

def create_skill(request):
	skill = Skill()
	skill.user = request.user
	skill.name = request.POST['name']
	skill.save()
	return HttpResponseRedirect(reverse('resume:skills'))

def delete_skill(request, id):
	skill = get_object_or_404(Skill, id=id)
	skill.delete()
	return HttpResponseRedirect(reverse('resume:skills'))


################################# SETTINGS

def settings(request):
	user = request.user
	profile = get_object_or_404(UserProfile, user=user)
	context = {
		'username': user.username,
		'email': user.email,
		'theme': profile.color,
	}
	return render(request, 'resume/settings.html', context)

def set_blue(request):
	user = request.user
	profile = get_object_or_404(UserProfile, user=user)
	profile.color = 'blue'
	profile.save()
	return HttpResponseRedirect(reverse('resume:settings'))

def set_green(request):
	user = request.user
	profile = get_object_or_404(UserProfile, user=user)
	profile.color = 'green'
	profile.save()
	return HttpResponseRedirect(reverse('resume:settings'))

def set_orange(request):
	user = request.user
	profile = get_object_or_404(UserProfile, user=user)
	profile.color = 'orange'
	profile.save()
	return HttpResponseRedirect(reverse('resume:settings'))

def set_pink(request):
	user = request.user
	profile = get_object_or_404(UserProfile, user=user)
	profile.color = 'pink'
	profile.save()
	return HttpResponseRedirect(reverse('resume:settings'))


################################# BUILD RESUME

def generate_resume(request, *args, **kwargs):
	profile = get_object_or_404(UserProfile, user=request.user)
	experiences = Experience.objects.filter(user=request.user)
	educations = Education.objects.filter(user=request.user)
	skills = Skill.objects.filter(user=request.user)
	context = {
		'full_name': request.user.first_name + ' '  + request.user.last_name,
		#'email': user.email, 
		'profession': profile.profession,
		'about_me': profile.bio,
		'experiences': experiences,
		'educations': educations,
		'skills': skills,
		'theme': profile.color,
	}
	pdf = render_to_pdf('pdf/test.html', context)
	if pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		download = request.GET.get("download")
		if download == 'True':
			response['Content-Disposition'] = 'attachment; filename=test.pdf'
		return response
	return HttpResponse('PDF not found')


from django.shortcuts import render, redirect, get_object_or_404 
from django.db.models import Q 
from django.contrib.auth.decorators import login_required 
from django.urls import reverse, reverse_lazy  
from django.contrib import messages 
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from .models import *
from .forms import *


# Create your views here.
def homepage_list_view(request):
	about_obj = About.objects.all().last()
	context = {
		'title':'Homepage',
		'about_obj':about_obj,
	}
	return render(request, 'blog/homepage_list.html', context)


# Functions For Pregnancy
def pregnancy_list_view(request):
	pregnancy_obj = Pregnancy.objects.filter(author=request.user)
	context = {
		'title':'Pregnancy list',
		'pregnancy_obj':pregnancy_obj
	}
	return render(request, 'blog/pregnancy_list.html', context)


def pregnancy_detail_view(request, pk):
	obj = get_object_or_404(Pregnancy, id=pk)
	context = {
		'title':'Pregnancy Details',
		'obj':obj
	}
	return render(request, 'blog/pregnancy_detail.html', context)


@login_required
def pregnancy_create_view(request):
	if request.method == 'POST':
		form = PregnancyForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			messages.success(request, f'Your post has been successfully created!')
			return redirect('pregnancy_detail', pk=instance.pk)
	else:
		form = PregnancyForm()

	context = {
		'title':'Post Create',
		'form':form,
	}
	return render(request, 'blog/prognancy_form.html', context)


@login_required
def pregnancy_update_view(request, pk):
	obj = get_object_or_404(Pregnancy, pk=pk)
	if request.method == 'POST' and obj.author == request.user:
		form = PregnancyForm(request.POST, instance=obj)
		if form.is_valid():
			form.save()
			messages.success(request, f'The post has been updated!')
			return redirect('pregnancy_detail', pk=obj.pk)
	else:
		form = PregnancyForm(instance=obj)

	context = {
		'title':'Post Update',
		'form':form,
	}
	return render(request, 'blog/prognancy_form.html', context)


@login_required
def pregnancy_delete_view(request, pk):
	obj = Pregnancy.objects.filter(pk=pk, author=request.user)
	obj.delete()
	messages.success(request, f'Your post has been deleted!')
	return redirect('pregnancy_list')


# Functions For Menopause
@login_required
def menopause_list_view(request):
	menepause_obj = Menopause.objects.filter(author=request.user)
	context = {
		'title':'Menopause list',
		'menepause_obj':menepause_obj
	}
	return render(request, 'blog/menepause_list.html', context)


@login_required
def menopause_detail_view(request, pk):
	obj = get_object_or_404(Menopause, id=pk)
	context = {
		'title':'Menopause Details',
		'obj':obj
	}
	return render(request, 'blog/menepause_detail.html', context)


@login_required
def menopause_create_view(request):
	if request.method == 'POST':
		form = MenopauseForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			messages.success(request, f'Your post has been successfully created!')
			return redirect('menopause_detail', pk=instance.pk)
	else:
		form = MenopauseForm()

	context = {
		'title':'Post Create',
		'form':form,
	}
	return render(request, 'blog/menopause_form.html', context)


@login_required
def menopause_update_view(request, pk):
	obj = get_object_or_404(Menopause, pk=pk)
	if request.method == 'POST' and obj.author == request.user:
		form = MenopauseForm(request.POST, instance=obj)
		if form.is_valid():
			form.save()
			messages.success(request, f'The post has been updated!')
			return redirect('menopause_detail', pk=obj.pk)
	else:
		form = MenopauseForm(instance=obj)

	context = {
		'title':'Post Update',
		'form':form,
	}
	return render(request, 'blog/menopause_form.html', context)


@login_required
def menopause_delete_view(request, pk):
	obj = Menopause.objects.filter(pk=pk, author=request.user)
	obj.delete()
	messages.success(request, f'Your post has been deleted!')
	return redirect('menopause_list')


# Intercourse
@login_required
def intercourse_list_view(request):
	intercourse_obj = Intercourse.objects.filter(author=request.user)
	context = {
		'title':'Intercourse list',
		'intercourse_obj':intercourse_obj
	}
	return render(request, 'blog/intercourse_list.html', context)


@login_required
def intercourse_detail_view(request, pk):
	obj = get_object_or_404(Intercourse, id=pk)
	context = {
		'title':'Intercourse Details',
		'obj':obj
	}
	return render(request, 'blog/intercourse_detail.html', context)


@login_required
def intercourse_create_view(request):
	if request.method == 'POST':
		form = IntercourseForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			messages.success(request, f'Your post has been successfully created!')
			return redirect('intercourse_detail', pk=instance.pk)
	else:
		form = IntercourseForm()

	context = {
		'title':'Post Create',
		'form':form,
	}
	return render(request, 'blog/intercourse_form.html', context)


@login_required
def intercourse_update_view(request, pk):
	obj = get_object_or_404(Intercourse, pk=pk)
	if request.method == 'POST' and obj.author == request.user:
		form = IntercourseForm(request.POST, instance=obj)
		if form.is_valid():
			form.save()
			messages.success(request, f'The post has been updated!')
			return redirect('intercourse_detail', pk=obj.pk)
	else:
		form = IntercourseForm(instance=obj)

	context = {
		'title':'Post Update',
		'form':form,
	}
	return render(request, 'blog/intercourse_form.html', context)


@login_required
def intercourse_delete_view(request, pk):
	obj = Intercourse.objects.filter(pk=pk, author=request.user)
	obj.delete()
	messages.success(request, f'Your post has been deleted!')
	return redirect('intercourse_list')


# Ovulation
@login_required
def ovulation_list_view(request):
	ovulation_obj = Ovulation.objects.filter(author=request.user)
	context = {
		'title':'Ovulation list',
		'ovulation_obj':ovulation_obj
	}
	return render(request, 'blog/ovulation_list.html', context)
	

@login_required
def ovulation_detail_view(request, pk):
	obj = get_object_or_404(Ovulation, id=pk)
	context = {
		'title':'Ovulation Details',
		'obj':obj
	}
	return render(request, 'blog/ovulation_detail.html', context)


@login_required
def ovulation_create_view(request):
	if request.method == 'POST':
		form = OvulationForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			messages.success(request, f'Your post has been successfully created!')
			return redirect('ovulation_detail', pk=instance.pk)
	else:
		form = OvulationForm()

	context = {
		'title':'Post Create',
		'form':form,
	}
	return render(request, 'blog/ovulation_form.html', context)


@login_required
def ovulation_update_view(request, pk):
	obj = get_object_or_404(Ovulation, pk=pk)
	if request.method == 'POST' and obj.author == request.user:
		form = OvulationForm(request.POST, instance=obj)
		if form.is_valid():
			form.save()
			messages.success(request, f'The post has been updated!')
			return redirect('ovulation_detail', pk=obj.pk)
	else:
		form = OvulationForm(instance=obj)

	context = {
		'title':'Post Update',
		'form':form,
	}
	return render(request, 'blog/ovulation_form.html', context)


@login_required
def ovulation_delete_view(request, pk):
	obj = Ovulation.objects.filter(pk=pk, author=request.user)
	obj.delete()
	messages.success(request, f'Your post has been deleted!')
	return redirect('ovulation_list')


# Functions For Menstruation
@login_required
def menstruation_list_view(request):
	menstruation_obj = Menstruation.objects.filter(author=request.user)
	context = {
		'title':'Menstruation list',
		'menstruation_obj':menstruation_obj
	}
	return render(request, 'blog/menstruation_list.html', context)


@login_required
def menstruation_detail_view(request, pk):
	obj = get_object_or_404(Menstruation, id=pk)
	context = {
		'title':'Menstruation Details',
		'obj':obj
	}
	return render(request, 'blog/menstruation_detail.html', context)


@login_required
def menstruation_create_view(request):
	if request.method == 'POST':
		form = MenstruationForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			messages.success(request, f'Your post has been successfully created!')
			return redirect('menstruation_detail', pk=instance.pk)
	else:
		form = MenstruationForm()

	context = {
		'title':'Post Create',
		'form':form,
	}
	return render(request, 'blog/menstruation_form.html', context)


@login_required
def menstruation_update_view(request, pk):
	obj = get_object_or_404(Menstruation, pk=pk)
	if request.method == 'POST' and obj.author == request.user:
		form = MenstruationForm(request.POST, instance=obj)
		if form.is_valid():
			form.save()
			messages.success(request, f'The post has been updated!')
			return redirect('menstruation_detail', pk=obj.pk)
	else:
		form = MenstruationForm(instance=obj)

	context = {
		'title':'Post Update',
		'form':form,
	}
	return render(request, 'blog/menstruation_form.html', context)


@login_required
def menstruation_delete_view(request, pk):
	obj = Menstruation.objects.filter(pk=pk, author=request.user)
	obj.delete()
	messages.success(request, f'Your post has been deleted!')
	return redirect('ovulation_list')
























# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import BMForm, UserForm
from .models import BMLog

# Create your views here.
def index(request):
    context = {}

    form = BMForm()
    context["form"] = form

    return render(request, 'gutlife_app/index.html', context)

def get_data(request):
    user_logs = BMLog.objects.filter(user=request.user)
    all_data = {}
    id=0
    for log in user_logs:
        log_data = {}
        log_data['consistency'] = log.consistency
        log_data['solidity'] = log.solidity
        log_data['datecode'] = log.datecode
        log_data['time'] = log.time
        all_data[id] = log_data
        id += 1

    return JsonResponse(all_data)

def post(request):
    if request.method == "POST":
        form = BMForm(request.POST)
        if form.is_valid():
            formConsistency = form.cleaned_data['consistency']
            formSolidity = form.cleaned_data['solidity']
            formDatecode = form.cleaned_data['datecode']
            formTime = form.cleaned_data['time']
            log = BMLog(consistency=formConsistency, solidity=formSolidity, datecode=formDatecode, time=formTime, user=request.user)
            log.save()
            return redirect('/dashboard/')
    return redirect('/dashboard')

def adduser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            messages.info(request, 'Account created successfully!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserForm()
    return render(request, 'gutlife_app/create_account.html', {'form': form})
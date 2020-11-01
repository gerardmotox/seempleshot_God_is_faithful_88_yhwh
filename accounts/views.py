# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import ImageUpload, MainCategories
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserSignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decorators import *

from django.views import View

@unauthenticated_user
def home(request):
    images = ImageUpload.objects.all().order_by('date_created')
    categories = MainCategories.objects.all().order_by('?')[:4]
    return render(request, "index.html", {'images': images, 'categories': categories})

def discover(request):
    return render(request, "discover.html")

def forgot_password(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, "forgot_password.html")

@login_required(login_url='login')
# @allowed_users(allowed_roles=['client'])
def userdashboard(request):
    return render(request, "dashboard.html")

@unauthenticated_user
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutuser(request):
    logout(request)
    return redirect("login")

@unauthenticated_user
def usersignup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # group = Group.objects.get(name='client')
            # form.groups.add(group)

            current_site = get_current_site(request)
            email_subject = 'Welcome to SeempleShot, activate your account to get started!'
            message = render_to_string('activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return render(request, 'account_created.html', {'emails': to_email})
    else:
        form = UserSignUpForm()
    return render(request, 'register.html', {'form': form})

@unauthenticated_user
def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'acount_activated.html')
    else:
        return render(request, 'acount_not_activated.html')

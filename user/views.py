from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


class UserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        field_classes = {'username': UsernameField}

def profile(request):
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)  # Important!
        messages.success(request, 'Your password was successfully updated!')
        return redirect('change_password')
    else:
        messages.error(request, 'Please correct the error below.')
    return render(request, 'user/profile.html', { 'form': form })

def password_change(request):
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)  # Important!
        messages.success(request, 'Your password was successfully updated!')
        return redirect('/user/profile/')
    else:
        messages.error(request, 'Please correct the error below.')
    return render(request, 'user/password_change.html', { 'form': form })

def register(request):
    user_form = UserForm(request.POST or None)
    if user_form.is_valid():
        user_form.save()
        return redirect('/user/login/')
    return render(request, 'user/registration.html', { 'user_form': user_form })

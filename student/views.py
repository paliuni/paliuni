from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


class UserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        field_classes = {'username': UsernameField}

def register(request):
    student_form = UserForm(request.POST or None)
    if student_form.is_valid():
        student_form.save()
        return redirect('/student/login/')
    return render(request, 'student/registration.html', { 'student_form': student_form })

def profile(request):
    courses = request.user.course_info_set.all()
    return render(request, 'student/profile.html', { 'courses': courses })

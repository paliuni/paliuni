from django.shortcuts import render
from blog.models import Blog
from instructors.models import Instructor
from django import forms
from user.models import Info
from django.core.mail import send_mail
from django.utils.translation import gettext as _


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'


def home(request):
    blogs = Blog.objects.all()
    instructors = Instructor.objects.all()
    form = InfoForm(request.POST or None)
    if form.is_valid():
        cd = form.cleaned_data
        name = cd['name']
        email = cd['email']
        mobile = cd['mobile']
        message = cd['message']
        form.save()
        send_mail(
                name,
                name + '\n' + email + '\n' + mobile + '\n' + message,
                'bpcht.japan@gmail.com',
                ['bpcht.japan@gmail.com'],
                )

        return render(request, 'home/index.html', { 'form': form, 'blogs': blogs, 'instructors': instructors })
    else:
        return render(request, 'home/index.html', { 'form': form, 'blogs': blogs, 'instructors': instructors })


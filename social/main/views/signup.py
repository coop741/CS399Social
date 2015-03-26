from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(data = request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect ("/signedup/")
    elif request.method == 'GET':
        form = SignupForm()
    else:
        return HttpResponseRedirect ("/404/")
    return render(request, "registration/signup.html", {"form": form})





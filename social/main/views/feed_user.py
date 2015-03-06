from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def feed_user(request, user_name):
    poster = get_object_or_404(User, username=user_name)
    return render(request, "main/feed_user.html", {'poster': poster})

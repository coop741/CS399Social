from django.shortcuts import render

def signedup(request):
    return render(request, "registration/signedup.html", {})

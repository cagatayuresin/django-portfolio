from django.shortcuts import render
from .models import CV


def index(request):
    cv = CV.objects.all()[0]
    return render(request, "cv.html", {"cv": cv})

from django.shortcuts import render
from .models import About

def AboutPage(request):
    about_us=About.objects.all()
    context={'about_us':about_us}
    return render(request,'about-us.html',context)

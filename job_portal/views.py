from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    members=Team_Members.objects.all()
    blogs=Blogs.objects.all()
    args = {'members':members, 'blogs':blogs}
    return render(request, 'job_portal/index.html', args)

def portal(request):
    return render(request,'job_portal/portal.html')

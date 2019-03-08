from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, redirect,get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    members=Team_Members.objects.all()
    blogs=Blogs.objects.all()
    form = Messageform(request.POST or None)
    args = {'members':members, 'blogs':blogs, 'form':form,}
    return render(request, 'job_portal/index.html', args)

def portal(request):
    return render(request,'job_portal/portal.html')

def index(request):
    form = Messageform(request.POST or None)
    if  request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request, 'job_portal/index.html', {'form': form})

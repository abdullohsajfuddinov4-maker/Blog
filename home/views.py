from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    project = Project.objects.all().order_by('-id')
    context = {'project':project}

    return render(request,'index.html',context)

def project(request,pk):
    project =Project.objects.filter(pk=pk).order_by('-id')
    context = {'project':project}
    return render(request,'page-portfolio.html',context)

def page_404(request):
    return render(request,'page-404.html')
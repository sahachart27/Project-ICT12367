from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import JobApplication
from .forms import JobApplicationForm

def home(request):
    applications = JobApplication.objects.all()
    return render(request, 'job_application/home.html', {'applications': applications})

def add_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "บันทึกข้อมูลผู้สมัครเรียบร้อยแล้ว!")
            return redirect('home')
    else:
        form = JobApplicationForm()
    
    return render(request, 'job_application/add_application.html', {'form': form})

def edit_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, "แก้ไขข้อมูลผู้สมัครเรียบร้อยแล้ว!")
            return redirect('home')
    else:
        form = JobApplicationForm(instance=application)
    
    return render(request, 'job_application/edit_application.html', {'form': form})

def delete_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    application.delete()
    messages.success(request, "ลบข้อมูลผู้สมัครเรียบร้อยแล้ว!")
    return redirect('home')

def search_application(request):
    query = request.GET.get('q', '')
    applications = JobApplication.objects.filter(
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(position_applied__icontains=query)
    )
    return render(request, 'job_application/home.html', {'applications': applications, 'query': query})

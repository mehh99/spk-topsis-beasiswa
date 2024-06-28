from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def dashboard(request):
    return render(request, 'dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def wakil_kesiswaan_dashboard (request):
    return render(request, 'wakil_kesiswaan_dashboard.html')
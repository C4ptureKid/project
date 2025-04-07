from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'public/index.html')

def login(request):
    return render(request, 'public/login.html')

def admin_home(request):
    return render(request, 'admin/admin_home.html')

def change_passkey(request):
    return render(request, 'admin/change_passkey.html')

def view_appreview_and_rating(request):
    return render(request, 'admin/view_appreview_and_rating.html')

def view_users(request):
    return render(request, 'admin/view_users.html')

def view_complaints_sendreply(request):
    return render(request, 'admin/view_complaints_sendreply.html')
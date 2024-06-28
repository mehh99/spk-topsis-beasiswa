from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# user/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import LoginHistory


@login_required
def user_main(request):
    current_user = request.user
    all_users = User.objects.all()
    return render(request, 'user.html', {'user': current_user, 'all_users': all_users})

def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Register Berhasil, Silahkan login')
                return redirect('register')
            else:
                messages.error(request, 'password dan konfirmasi password tidak sesuai')
                return render(request, 'register.html', {'form':form})
    else:
        form = RegisterForm()
        return render (request, 'register.html', {'form' : form})
    
def delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('user')




def user_login_history(request, user_id):
    user = get_object_or_404(User, id=user_id)
    login_history = LoginHistory.objects.filter(user=user).order_by('login_time')[:10]
    return render(request, 'user_login_history.html', {'user': user, 'login_history': login_history})








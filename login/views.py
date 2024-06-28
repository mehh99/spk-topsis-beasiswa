from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from dashboard.views import dashboard
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'main.html')



from django.contrib.auth import authenticate
from user.models import LoginHistory

from django.utils import timezone
from user.models import LoginHistory

# ...

def handle_login(request, username, password):
    user = authenticate(request, username=username, password=password)

    if user is not None:
        if user.check_password(password):
            # Login berhasil
            login(request, user)

            # Catat history login
            LoginHistory.objects.create(user=user, success=True, login_time=timezone.now())

            # Lanjutkan ke dashboard atau halaman setelah login
            return True
    # Catat history login gagal
    LoginHistory.objects.create(username=username, success=False, login_time=timezone.now())

    # Berikan respons login gagal
    return False


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
            
#             if user is not None:
#                 # Menggunakan fungsi handle_login untuk autentikasi
#                 if handle_login(request, username, password):
#                     login(request, user)
                    
#                     # Periksa apakah pengguna memiliki akses sebagai admin atau wakil kesiswaan
#                     if user.is_superuser and request.POST.get('user_role') != 'admin':
#                         messages.error(request, 'Anda tidak dapat login sebagai wakil kesiswaan.')
#                         return render(request, 'login.html', {'form': form})
#                     elif not user.is_superuser and request.POST.get('user_role') != 'wakil_kesiswaan':
#                         messages.error(request, 'Anda tidak dapat login sebagai admin.')
#                         return render(request, 'login.html', {'form': form})

#                     # Lanjutkan ke dasbor yang sesuai dengan rolenya
#                     if user.is_superuser:
#                         return redirect('admin_dashboard')  # Alihkan ke dasbor admin
#                     else:
#                         return redirect('wakil_kesiswaan_dashboard')  # Alihkan ke dasbor wakil kesiswaan

#                 else:
#                     # Jika handle_login mengembalikan False (login gagal)
#                     messages.error(request, 'Username atau password salah. Coba lagi!')
#                     return render(request, 'login.html', {'form': form})
#             else:
#                 messages.error(request, 'Username atau password salah. Coba lagi!')
#                 return render(request, 'login.html', {'form': form})
#         else:
#             messages.error(request, 'Silahkan centang salah satu role.')
#             return render(request, 'login.html', {'form': form})
#     else:
#         form = LoginForm()
#         return render(request, 'login.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Menggunakan fungsi handle_login untuk autentikasi
                if handle_login(request, username, password):
                    login(request, user)
                    
                    # Periksa apakah pengguna memiliki akses sebagai admin atau wakil kesiswaan
                    if user.is_superuser and request.POST.get('user_role') != 'admin':
                        return redirect('wakil_kesiswaan_dashboard')
                    elif not user.is_superuser and request.POST.get('user_role') != 'wakil_kesiswaan':
                        messages.error(request, 'Anda tidak dapat login sebagai admin.')
                        return render(request, 'login.html', {'form': form})

                    # Lanjutkan ke dasbor yang sesuai dengan rolenya
                    if user.is_superuser:
                        return redirect('admin_dashboard')  # Alihkan ke dasbor admin
                    else:
                        return redirect('wakil_kesiswaan_dashboard')  # Alihkan ke dasbor wakil kesiswaan

                else:
                    # Jika handle_login mengembalikan False (login gagal)
                    messages.error(request, 'Username atau password salah. Coba lagi!')
                    return render(request, 'login.html', {'form': form})
            else:
                messages.error(request, 'Username atau password salah. Coba lagi!')
                return render(request, 'login.html', {'form': form})
        else:
            messages.error(request, 'Silahkan centang salah satu role.')
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    
def user_logout(request):
    logout(request)
    return redirect('login')


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Metodos de vistas AUTH
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecciona al usuario a la página de inicio si las credenciales son correctas
        else:
            error_message = 'Credenciales inválidas. Por favor, intenta nuevamente.'
    else:
        error_message = ''
    return render(request, 'login.html', {'error_message': error_message})

def logout_user(request):
    logout(request)
    return redirect('login')

########################################################################################################################

#Metodos Vistas (auth = True)

def home(request):
    if not request.user.is_authenticated: # En produccion cambiar a: if request.user.is_authenticated (sin el not)
        return render(request, 'home.html')
    else:
        return redirect('login')
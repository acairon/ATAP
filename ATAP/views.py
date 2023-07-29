from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Metodos de AUTH
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

#Metodos Vistas

def home(request):
    return render(request, 'home.html')
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from ATAP.forms import TaskForm
from ATAP.models import Tasks


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
        return render(request, 'home.html')

########################################################################################################################

#Metodos tareas

def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user  # Asigna al usuario actual como el creador de la tarea
            task.created_at = timezone.now()
            task.updated_at = timezone.now()
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

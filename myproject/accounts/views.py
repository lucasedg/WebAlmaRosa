from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Reemplaza 'home' por la URL a la que quieras redirigir después del inicio de sesión
        else:
            # Manejar error de inicio de sesión inválido
            pass
    return render(request, 'login.html')  # Reemplaza 'login.html' con la plantilla de inicio de sesión

def logout_view(request):
    logout(request)
    return redirect('login')  # Reemplaza 'login' por el nombre de la URL de inicio de sesión

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Reemplaza 'home' por la URL a la que quieras redirigir después del registro
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})  # Reemplaza 'register.html' con la plantilla de registro

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Hola! Esta es la página de inicio de tu aplicación.")

from django.shortcuts import render
from .models import Dueño, Paciente, Veterinario
from .forms import DueñoForm, PacienteForm, VeterinarioForm
from django.contrib import messages

def home(request):
    return render(request, 'gestion/home.html')

from django.shortcuts import render, redirect

from .forms import DueñoForm, PacienteForm, VeterinarioForm

def registrar_dueño(request):
    if request.method == 'POST':
        form = DueñoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro de dueño exitoso!')  #
            return redirect('registrar_dueño') 
    else:
        form = DueñoForm()
    return render(request, 'gestion/formulario.html', {'form': form, 'titulo': 'Registrar Dueño'})

def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro de paciente exitoso!')  
            return redirect('registrar_paciente')
    else:
        form = PacienteForm()
    return render(request, 'gestion/formulario.html', {'form': form, 'titulo': 'Registrar Paciente'})

def registrar_veterinario(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro de veterinario exitoso!')  
            return redirect('registrar_veterinario')
    else:
        form = VeterinarioForm()
    return render(request, 'gestion/formulario.html', {'form': form, 'titulo': 'Registrar Veterinario'})

def buscar(request):
    if 'q' in request.GET:
        query = request.GET['q']
        resultados = Paciente.objects.filter(nombre__icontains=query)
    else:
        resultados = None
    return render(request, 'gestion/buscar.html', {'resultados': resultados})
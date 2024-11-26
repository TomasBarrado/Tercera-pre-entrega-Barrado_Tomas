from django import forms
from .models import Dueño, Paciente, Veterinario

class DueñoForm(forms.ModelForm):
    class Meta:
        model = Dueño
        fields = '__all__'

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = '__all__'

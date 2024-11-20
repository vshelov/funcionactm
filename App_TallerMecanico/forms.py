# App_TallerMecanico/forms.py

from django import forms
from django.utils import timezone
from .models import Trabajo, Vehiculo, Mecanico

class TrabajoForm(forms.ModelForm):
    fecha_ingreso = forms.DateTimeField(
        initial=timezone.now,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Fecha de Ingreso'
    )
    fecha_entrega = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Fecha de Entrega'
    )
    estado = forms.ChoiceField(
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_progreso', 'En Progreso'),
            ('completado', 'Completado'),
        ],
        label='Estado'
    )

    class Meta:
        model = Trabajo
        fields = ['vehiculo', 'mecanico', 'estado', 'costo_total_reparaciones', 'fecha_ingreso', 'fecha_entrega']
        widgets = {
            'costo_total_reparaciones': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'vehiculo': 'Vehículo',
            'mecanico': 'Mecánico',
            'costo_total_reparaciones': 'Costo Total Reparaciones',
        }

    def clean_costo_total_reparaciones(self):
        costo = self.cleaned_data.get('costo_total_reparaciones')
        if costo < 0:
            raise forms.ValidationError("El costo total de reparaciones no puede ser negativo.")
        return costo

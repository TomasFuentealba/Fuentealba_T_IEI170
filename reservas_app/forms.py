from django import forms
from reservas_app.models import Reserva
from django.core.validators import RegexValidator

class FormReserva(forms.ModelForm):
    observacion = forms.CharField(required=False)
    nombre_persona = forms.CharField(
        max_length=80,
        min_length=2,
        error_messages={
            'max_length': 'El nombre no puede tener más de 80 caracteres.',
            'min_length': 'El nombre debe tener al menos 2 caracteres.'
        }
    )

    telefono = forms.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^[\d\+]+$'
            )
        ]
    )

    cantidad_personas = forms.IntegerField(min_value=1, max_value=15)


    class Meta:
        model = Reserva
        fields = '__all__'

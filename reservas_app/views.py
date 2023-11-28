from django.shortcuts import render,redirect
from reservas_app.models import Reserva
from reservas_app.forms import FormReserva

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listadoReserva(request):
    reservas = Reserva.objects.all()
    data = {'reserva': reservas}
    return render(request, 'reservas.html', data)

def agregarReserva(request):
    form = FormReserva()

    if (request.method == 'POST'):
        form = FormReserva(request.POST)
        if (form.is_valid()):
            form.save()
            return index(request)
  
    data = {'form': form}
    return render (request, 'agregar.html', data)

def eliminarReserva(request, IN_id):
    reserva = Reserva.objects.get(id = IN_id)
    reserva.delete()
    return redirect('/reservas')

def modificarReserva(request, IN_id):
    reserva = Reserva.objects.get(id = IN_id)
    form = FormReserva(instance=reserva)

    if (request.method == 'POST'):
        form = FormReserva(request.POST, instance=reserva)
        if (form.is_valid()):
            form.save()
            return redirect('/reservas')
  
    data = {'form': form}
    return render (request, 'agregar.html', data)
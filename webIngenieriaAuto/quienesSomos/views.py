from django.shortcuts import render
from .models import Empleado
# Create your views here.


def quienes_somos(request):
    empleados = Empleado.objects.all()
    return render(request,"quienesSomos/quienes-somos.html", {'empleados': empleados})
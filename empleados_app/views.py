from django.shortcuts import render,redirect
from .models import Empleado

# Create your views here.
def index_Empleado(request):
    nEmpleado=Empleado.objects.all()
    return render(request,'gestEmp.html',{'mEmpleado':nEmpleado})

def regisEmpleado(request): 
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtape"]
    numero=request.POST["num"]
    sexo=request.POST["txtsex"]
    puesto=request.POST["txtpue"]
    salario=request.POST["numsal"]
    direc=request.POST["txtdir"]
    
    guarEmpleado=Empleado.objects.create(
            id_empleado=id,nombre=nombre,apellido=apellido,numero=numero,sexo=sexo,puesto=puesto,salario=salario,direccion=direc
    )
    return redirect("Empleado")

def selecEmp(request,id):
    emp=Empleado.objects.get(id_empleado=id)
    return render(request,'editarEmp.html',{"mEmpleado":emp})

def editEmp(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtape"]
    numero=request.POST["num"]
    sexo=request.POST["txtsex"]
    puesto=request.POST["txtpue"]
    salario=request.POST["numsal"]
    direc=request.POST["txtdir"]
    emp=Empleado.objects.get(id_empleado=id)
    emp.nombre=nombre
    emp.apellido=apellido
    emp.numero=numero
    emp.sexo=sexo
    emp.puesto=puesto  
    emp.salario=salario
    emp.direccion=direc 
    emp.save()
    return redirect('Empleado')

def borrarEmp(request,id):
    emp=Empleado.objects.get(id_empleado=id)
    emp.delete()
    return redirect('Empleado')


from django.urls import path
from empleados_app import views

urlpatterns = [
    path('Empleado',views.index_Empleado,name='Empleado'),
    path('regisEmpleado/',views.regisEmpleado,name='regisEmpleado'),
    path('selecEmp/<id>',views.selecEmp,name="selecEmp"),
    path('editEmp/',views.editEmp,name="editEmp"),
    path('borrarEmp/<id>',views.borrarEmp,name="borrarEmp"),
]
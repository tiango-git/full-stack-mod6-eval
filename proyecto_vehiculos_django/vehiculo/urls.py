from django.urls import path
from .views import indexView, addVehiculo, registro_view, login_view, logout_view, listar_vehiculo

urlpatterns = [
    path('', indexView, name='index'),
    path('add/', addVehiculo, name='addform'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('listar/', listar_vehiculo, name='listar')

]

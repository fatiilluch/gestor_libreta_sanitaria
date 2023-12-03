# En gestion_mascotas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_pet/', views.newPet, name='new_pet'),
    path('select_pets/', views.selectPet, name='select_pets'),
    path('add_vacune/<int:pet_id>/', views.addVacune, name='add_vacune'),
    path('vacune_list/<int:pet_id>/', views.listVacunes, name='vacune_list'),
    path('delete_vacune/<int:vacune_id>/', views.deleteVacune, name='delete_vacune'),
    path('edit_vacune/<int:vacune_id>/', views.updateVaccine, name='edit_vacune'),
    path('edit_pet/<int:pet_id>/', views.updatePet, name='edit_pet'),

    # Otras URLS de la aplicación
]

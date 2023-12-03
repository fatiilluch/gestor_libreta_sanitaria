from django.shortcuts import render, get_object_or_404, redirect
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Pet, Vacune
from .forms import VacuneForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def newPet(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        specie = data.get('specie')
        birth_date = data.get('birth_date')
        breed = data.get('breed')
        color = data.get('color')
        
        # Create an instance of the pet model with the form data
        new_pet = Pet(name=name, specie=specie, 
                      birth_date=birth_date, breed=breed, color=color)
        
        print(new_pet)
        # save new pet instance to the database
        try:
            new_pet.save()
        except IntegrityError as e:
            raise IntegrityError (f"There was an error saving the pet instance. Error: {e}")
        else:
            return render(request, 'home.html')
    return render(request, 'new_pet.html')

def selectPet(request):
    pets = Pet.objects.all() # obtiene todos los registros de pet
    return render(request, 'select_pets.html', {'pets': pets})


def addVacune(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    
    if request.method == 'POST':
        pet_id = request.POST.get('pet_id')
        
        # get form data
        nombre = request.POST.get('nombre')
        dia_aplicacion = request.POST.get('dia_aplicacion')
        proxima_fecha = request.POST.get('proxima_fecha')
        
        # create the vacune instance
        new_vacune = Vacune(nombre=nombre, dia_aplicacion=dia_aplicacion, proxima_fecha=proxima_fecha)
        print(new_vacune)
        try:
            new_vacune.save()
            pet.vacunes.add(new_vacune)
        except IntegrityError as e:
            raise IntegrityError (f"There was an error saving the pet instance. Error: {e}")
        else:
            return HttpResponseRedirect(reverse('select_pets'))
    return render(request, 'add_vacune.html', {'pet': pet})

def listVacunes(request, pet_id):
    pet = Pet.objects.get(id=pet_id) # get the pet istance with the id = pet_id
    vacunes = pet.vacunes.all() # obtiene todos los registros de vacune de pet
    return render(request, 'vacune_list.html', {'pet': pet, 'vacunes': vacunes})

def deleteVacune(request, vacune_id):
    vacune = get_object_or_404(Vacune, pk=vacune_id)
    try:
        pet = Pet.objects.get(vacunes__id=vacune_id)
        pet_id = pet.id
        print(pet_id)
    except Pet.DoesNotExist:
        pet_id = None
    if pet_id is not None: 
        if request.method == 'POST':    
            if request.POST.get('confirmacion') == ("Confirmar eliminación"):
                vacune.delete() # delete the vacune
            return redirect(reverse('vacune_list', kwargs={'pet_id':pet_id}))
        else:
            return render(request, 'delete_vacune.html', {'vacune': vacune, 'pet_id':pet_id})
    else:
        return render(request, '404.html')
    
    
def updateVaccine(request, vacune_id):
    try:
        vacune = Vacune.objects.get(id=vacune_id)
        pet = Pet.objects.get(vacunes__id=vacune_id)
        pet_id = pet.id
    except Pet.DoesNotExist:
        return HttpResponseNotFound("<h1> Pet not found </h1>")
    except Vacune.DoesNotExist:
        return HttpResponseNotFound("<h1> Vacune not found </h1>")
    if request.method == 'POST':
        form = VacuneForm(request.POST, instance=vacune)
        print(form)  
        if form.is_valid():  
            form.save()
            return redirect('vacune_list', pet_id=pet_id)
    else:
        form = VacuneForm(instance=vacune)
        return render(request, 'edit_vacune.html', {'form': form, 'vacune': vacune, 'pet_id': pet_id})
            
def updatePet(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
        print(pet)
        return render(request, 'edit_pet.html', {'pet': pet})
    except Exception:
        return HttpResponseNotFound("<h1> Pet not found </h1>")
        
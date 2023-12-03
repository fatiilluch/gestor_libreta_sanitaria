from django.db import models

# Create your models here.

class Vacune(models.Model):
    nombre = models.CharField(max_length=50)
    dia_aplicacion = models.DateField()
    proxima_fecha = models.DateField()
    
    def __str__(self) -> str:
        return f"""
            name: {self.nombre},
            application date: {self.dia_aplicacion},
            next date: {self.proxima_fecha}
        """

class Antiparasitic(models.Model):
    nombre = models.CharField(max_length=50)
    dia_aplicacion = models.DateField()
    refuerzo = models.DateField() # esta es la primera instancia de pastillas. Los anteiparasitarios generalmente se dan a los 15 dias y luego a los otros 15 dias. 
    proxima_fecha = models.DateField()
    
    def __str__(self) -> str:
        return f"""
            name: {self.nombre},
            application date: {self.dia_aplicacion},
            booster: {self.refuerzo}.
            next date: {self.proxima_fecha}
        """
       

class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    specie = models.CharField(max_length=50)
    birth_date = models.DateField()
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    vacunes = models.ManyToManyField(Vacune, blank=True, related_name='pets')
    antiparasitic = models.ManyToManyField(Antiparasitic, blank=True, related_name='pets')
    
    
    def __str__(self) -> str:
        return f"""
            name: {self.name}, 
            specie: {self.specie},
            birth_date: {self.birth_date},
            breed: {self.breed},
            color: {self.color}
        """


import random
import numpy

class vehiculo:
    def __init__(self):
        self.avance = 0
        self.rendimiento = self.calcular_rendimiento()
        self.intentos = 0
        self.meta_alcanzada = False
    def calcular_rendimiento(self):
        print('no implementado')
        return 0
    def avanzar(self):
        if not self.meta_alcanzada:
            self.avance = self.avance + self.rendimiento
            self.intentos = self.intentos + 1



class camion(vehiculo):
    def calcular_rendimiento(self):
        fuerza_del_motor = random.randrange(10)
        return 2*(fuerza_del_motor)+1
    def __str__(self):
        return "Soy camion"
    def __repr__(self):
        return "Soy camion"
class tractor(vehiculo):
    def calcular_rendimiento(self):
        fuerza_del_motor = random.randrange(10)
        return numpy.log(2)*fuerza_del_motor
    def __str__(self):
        return "Soy tractor"
    def __repr__(self):

        return "Soy tractor"


class sedan(vehiculo):
    def calcular_rendimiento(self):
        fuerza_del_motor = random.randrange(10)
        return 3*((fuerza_del_motor)**2)
    def __str__(self):
        return "Soy sedan"
    def __repr__(self):
        return "Soy sedan"


class bus(vehiculo):
    def calcular_rendimiento(self):
        fuerza_del_motor = random.randrange(10)
        return 5*(fuerza_del_motor)
    def __str__(self):
        return "Soy bus"
    def __repr__(self):
        return "Soy bus"


class carrera:
    def __init__(self):
        self.meta = 1000
        self.vehiculos = [camion(), tractor(), sedan(), bus()]
    def comenzar(self):
        llegada = False
        while not llegada:
            llegada = True
            for competidor in self.vehiculos:
                competidor.avanzar()
                if competidor.avance > 1000:
                    competidor.meta_alcanzada = True
                if not competidor.meta_alcanzada:
                    llegada = False

    def resultado(self):
        for competidor in self.vehiculos:
            print(competidor, 'avance:', competidor.avance, '/', 'Numero de intentos:', competidor.intentos,'/','Eficiencia de avance maxima:',competidor.rendimiento)
     #   print("First: ", min(self.vehiculos, key=lambda p: p.intentos))
        a = sorted(self.vehiculos, key=lambda x: x.intentos)
        print("First", a[0]);
        print("Secund", a[1]);


LaCarrera = carrera()
LaCarrera.comenzar()
LaCarrera.resultado()



from i_vehicle import IVehicle

class Car(IVehicle):

    def ignite(self):
        print("Encendiendo vehículo")

    def refuel(self):
        print("Recargando gasolina")
from ast import Pass


from car import Car
from truck import Truck

class Factory:
    
    @staticmethod
    def get_instance(type):
        
        if(type == 'truck'):
            return Truck()
        
        if(type == 'car'):
            return Car()

        raise ValueError(type)

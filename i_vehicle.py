from abc import ABC, abstractmethod

class IVehicle(ABC):

    @abstractmethod
    def ignite(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

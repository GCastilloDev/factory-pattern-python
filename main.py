from factory import Factory

vehicle = Factory().get_instance("car")

vehicle.ignite()
vehicle.refuel()
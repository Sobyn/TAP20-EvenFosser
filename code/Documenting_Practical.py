
class Car:
    """
    Creating the parent class 'Car', with numerous class variables
    """

    def __init__(self):
        """
        The 'Car' constructor
        """
        self.type = ""
        self.model = ""
        self.wheels = 4
        self.doors = 3
        self.seets = 5


    def print_model(self):
        """
        Method that retrieves the model and type from certain inherited classes
        """
        print("This car is a {model}: {type}, Wow!".format(model=self.model,type= self.type))


    def print_space(self):
        """
        Method that retrieves the amount of doors and seats from certain inherited classes
        """
        print("The car has {0} doors and {1} seets".format(self.doors, self.seets))


    def __str__(self):
        """
        Method that returns the result from the previous two methods
        """
        return """
This car is a {s.model}: {s.type}, Wow!
The car has {s.doors} doors and {s.seets} seets""".format(s=self)


class BMW(Car):
    """
    The 'BMW' class, inherited from 'Car'
    """

    def __init__(self, **arg):
        """
        The 'BMW' constructor, with the new class variable 'fuel'
        """

        Car.__init__(self)
        self.model = "BMW"
        self.type = "{} Series".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")


class Mercedes(Car):
    """
    The 'Mercedes' class, inherited from 'Car'
    """

    def __init__(self, **arg):
        """
        The 'Mercedes' constructor, also with the 'fuel' class variable
        """
        Car.__init__(self)
        self.model = "Mercedes"
        self.type = "{} Class".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")


class Fuel:
    """
    Creating the 'Fuel' class
    """

    def __init__(self, **arg):
        """
        The 'Fuel' constructor, with the variables 'liters' and 'type'
        """
        self.liters = arg.get("liters")
        self.type = arg.get("type")

    def __str__(self):
        """
        Method that returns the values of the variables in the previous method
        """
        return """It uses {s.liters}L of {s.type}¢.""".format(s=self)


class CarFactory:
    """
    Creating the class 'CarFactory'
    """

    def __init__(self, **kwargs):
        """
        The 'CarFactory' constructor
        """
        self.car = kwargs.get("type")(type=kwargs.get("car_type"),doors=kwargs.get("doors"),fuel=Fuel(liters=kwargs.get("liters"),type=kwargs.get("fuel_type")))

    def get_car(self):
        """
        A method 'get_car' which returns a car model
        """
        return self.car


class CarStore:
    """
    Creating the class 'CarStore'
    """
    inventory = []

    def __init__(self, **kwargs):
        """
        The 'CarStore' constructor, which collects various information and saves it to variables
        :param kwargs:
        """
        self._car_factory = CarFactory(type=kwargs.get("type"), car_type=kwargs.get("car_type"),doors=kwargs.get("doors"),liters=kwargs.get("liters"),fuel_type=kwargs.get("fuel_type"))
        self.inventory.append(self._car_factory.get_car())

    def show_car(self, car=None):
        """
        Method that runs if no car is present, which in that case is retrieved from 'CarFactory'
        :param car:
        :return:
        """
        if not car:
            car = self._car_factory.get_car()

        print(car)
        print(car.fuel)

    def show_inventory(self):
        """
        Method that shows inventory of 'CarStore'
        :return:
        """
        for i in self.inventory:
            self.show_car(i)

    def __str__(self):
        """
        Method that joins together items in inventory and returns it
        :return:
        """
        return "".join([str(i) for i in self.inventory])


store = CarStore(type=Mercedes, car_type= "E", doors=2, liters = 2,fuel_type = "Disel")
store2 = CarStore(type=Mercedes, car_type= "C", doors=4, liters = 2,fuel_type = "Disel")
store3 = CarStore(type=BMW, car_type="1", doors= 3, liters= 2.5, fuel_type = "Gasoline")
store.show_inventory()

print("\n","-"*100)


class Lada(Car):
    """
    Creating the 'Lada' class, which is inherited from 'Car'
    """
    def __init__(self, **arg):
        """
        The 'Lada' constructor
        :param arg:
        """
        Car.__init__(self)
        self.model = "Lada"
        self.type = "{}".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")


store = CarStore(type=Lada, car_type="VAZ-2107",doors=2,liters=1.2,fuel_type="Octane Gasoline")

store.show_inventory()
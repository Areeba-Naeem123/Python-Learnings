class Car:
    def __init__(self, brand , model):
        self.__brand = brand #private 
        self.model=model

    def print_car(self):
        print (f" Car brand: {self.get_brand()} \n Car model: {self.model}")

    def get_brand(self):
        return self.__brand

    def set_brand(self, newbrand):
        self.__brand=newbrand

    


# inheritence 

class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size



my_electric_car= Electric_car("tesla","model S", "85KWH")
# print(my_electric_car.model)
my_electric_car.print_car()
my_electric_car.set_brand("ayo ayo")
my_electric_car.print_car()

# mycar=Car("toyota","corola")
# mycar.print_car()

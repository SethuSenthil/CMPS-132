class Car:
        def __init__(self, __make, __model, __year):
            self.make = __make
            self.model = __model
            self.year = __year
            self.tankSize = 18

        def fill_up_tank(self, gal):
            self.tankSize += gal
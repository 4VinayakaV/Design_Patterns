
class Sedan:
    def drive(self):
        return "Driving a sedan"

class SUV:
    def drive(self):
        return "Driving an SUV"


class CarFactory:
    def create_car(self, car_type):
        if car_type == 'sedan':
            return Sedan()
        elif car_type == 'suv':
            return SUV()
        else:
            return None


if __name__ == "__main__":
    factory = CarFactory()

    sedan = factory.create_car('sedan')
    print(sedan.drive())

    suv = factory.create_car('suv')
    print(suv.drive())

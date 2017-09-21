
class Parking(object):
    def __init__(self, address, number_of_places):
        self.address = address
        self.number_of_places = number_of_places

    def try_accept_car(self, car, other_parkings=None):
        if self.number_of_places - car.size >= 0:
            print('OK')
            self.number_of_places -= car.size
        else:
            print('No space left!')
            if not other_parkings:
                return

            other_free_parking = None
            for p in other_parkings:
                if p.number_of_places - car.size >= 0:
                    other_free_parking = p
                    break

            if other_free_parking:
                print('Go to', other_free_parking.address)
                other_free_parking.try_accept_car(car)

class Car(object):
    size = 1
    acceptable = True

    def __init__(self, number, model):
        self.number = number
        self.model = model

class Truck(Car):
    size = 2

chertanovo = Parking('Chertanovo 54', 10)
butovo = Parking('Butovo 4', 20)

n = 110
for i in range(n):
    car = Car('x405ce', 'Honda')
    butovo.try_accept_car(
        car, other_parkings=[chertanovo, ])

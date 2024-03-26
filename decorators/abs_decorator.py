from cars.abs_car import AbsCars


class AbsDecorator(AbsCars):
    def __init__(self, car):
        self._car = car

    @property
    def car(self):
        return self._car
from cars.abs_car import AbsCars


class Luxury(AbsCars):
    @property
    def cost(self):
        return 100000

    @property
    def description(self):
        return "Luxury car"
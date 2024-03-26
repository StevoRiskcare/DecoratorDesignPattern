from cars.abs_car import AbsCars


class Economy(AbsCars):
    @property
    def cost(self):
        return 1000

    @property
    def description(self):
        return "Economy car"
from cars.abs_car import AbsCars


class Sport(AbsCars):
    @property
    def cost(self):
        return 1500

    @property
    def description(self):
        return "Sport car"
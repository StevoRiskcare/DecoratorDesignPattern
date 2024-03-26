from decorators.abs_decorator import AbsDecorator


class Red(AbsDecorator):
    @property
    def cost(self):
        return self.car.cost + 50

    @property
    def description(self):
        return self.car.description + ' in metalic red'
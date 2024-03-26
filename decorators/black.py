from decorators.abs_decorator import AbsDecorator


class Black(AbsDecorator):
    @property
    def cost(self):
        return self.car.cost + 150

    @property
    def description(self):
        return self.car.description + ' in black'

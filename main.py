from cars.economy import Economy
from cars.luxury import Luxury
from cars.sport import Sport
from decorators.black import Black
from decorators.red import Red


def main():
    car = Economy()
    car = Black(car)
    show_car(car)

    car = Luxury()
    car = Black(car)
    show_car(car)

    car = Sport()
    car = Red(car)
    show_car(car)


def show_car(car):
    print(car.cost, car.description)

if __name__ == '__main__':
    main()
import cars

def main():
    car_1 = cars.Car(122354, "Ford", "Focus", 2000, 200)
    car_2 = cars.Car(222235, "Porsche", "911 Turbo", 2023, 0)

    car_1.filler_up(20)
    car_2.filler_up(5)

    car_1.print_car()
    car_2.print_car()

    car_1.drive(100)
    car_2.drive(10)

    car_1.print_car()
    car_2.print_car()

    car_1_str = str(car_1)

    print(car_1_str)
    print(car_1)

if __name__ == "__main__":
    main()
class Transport:

    def stating_of_engine(self):
        print('Engine is started now!')
        print('Brrrrrrrrrr')

    def stop_engine(self):
        print('pshshshshhs')
        print("Engine is stoped")


class Motor_transport(Transport):
    fuel_for_100_km = 0
    traveled_distance = 0

    def __init__(self, fuel_for_100_km, traveled_distance):
        self.fuel_for_100_km = fuel_for_100_km
        self.traveled_distance = traveled_distance

    def used_fuel(self):
        return print('Used fuel for distance: ', self.traveled_distance / 100 * self.fuel_for_100_km)


class Car(Motor_transport):
    brand = ''
    model = ''
    year_of_production = 2000
    all_seats = 4
    occupied_seats = 0

    def __init__(self, brand, model, year_of_production, fuel_for_100_km, traveled_distance, all_seats=4,
                 occupied_seats=0):
        super().__init__(fuel_for_100_km, traveled_distance)
        self.brand = brand
        self.model = model
        self.year_of_production = year_of_production
        self.all_seats = all_seats
        self.occupied_seats = occupied_seats

    def full_name_of_car(self):
        return print(self.brand, self.model, str(self.year_of_production))

    def __free_seats_status(self):
        free_seats = self.all_seats - self.occupied_seats
        if free_seats > 0:
            return True
        else:
            return False

    def count_of_free_seats_status(self):
        if self.__free_seats_status == True:
            print(self.all_seats - self.occupied_seats)
        else:
            print('Car is full. You don"t have empty seats')

    def can_your_pick_up_sb(self):
        if self.__free_seats_status == True:
            print('Yes, you can to pick up some body')
        else:
            print('No, car is FULL')


class Truck(Motor_transport):
    name = ''
    maximum_possible_load_kg = 0
    loaded_weight_kg = 0

    def __init__(self, name, maximum_possible_load_kg, loaded_weight_kg, fuel_for_100_km, traveled_distance):
        super().__init__(fuel_for_100_km, traveled_distance)
        self.name = name
        self.maximum_possible_load_kg = maximum_possible_load_kg
        self.loaded_weight_kg = loaded_weight_kg

    def __index_of_congestion_weight(self):
        congestion_weight = (self.loaded_weight_kg / self.maximum_possible_load_kg) + 1
        return congestion_weight

    def used_fuel(self):
        return print('Used fuel for distance: ', (self.traveled_distance / 100 * self.fuel_for_100_km) * self.__index_of_congestion_weight())


def main():
    my_car = Car('Honda', 'Sivik', 2000, 9.8, 19900, 5, 1)
    my_car.full_name_of_car()
    my_car.count_of_free_seats_status()
    my_car.can_your_pick_up_sb()
    my_car.used_fuel()
    my_track = Truck('Skania', 10005, 9005, 30.5, 3956)
    my_track.used_fuel()


if __name__ == "__main__":
    main()

import random
import json

class ParkingLot:
    def __init__(self, square_footage, spot_size=(8, 12)):
        self.square_footage = square_footage
        self.spot_size = spot_size
        self.parking_spots = [None] * self.calculate_spots()

    def calculate_spots(self):
        spot_area = self.spot_size[0] * self.spot_size[1]
        return self.square_footage // spot_area

    def park_car(self, car, spot):
        if self.parking_spots[spot] is None:
            self.parking_spots[spot] = car
            return True
        else:
            return False

    def map_to_json(self):
        mapping = {f"Spot {i+1}": str(car) if car else "Empty" for i, car in enumerate(self.parking_spots)}
        return json.dumps(mapping, indent=2)


class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

    def park(self, parking_lot):
        spot = random.randint(0, len(parking_lot.parking_spots) - 1)
        while not parking_lot.park_car(self, spot):
            spot = random.randint(0, len(parking_lot.parking_spots) - 1)
        return spot


def main():
    parking_lot_size = 2000
    car_count = 20
    parking_spot_size = (8, 12)

    parking_lot = ParkingLot(parking_lot_size, parking_spot_size)
    cars = [Car(f"acb412{i}") for i in range(car_count)]

    for car in cars:
        spot = car.park(parking_lot)
        if spot is not None:
            print(f"Car with license plate {car} parked successfully in spot {spot + 1}")
        else:
            print(f"Car with license plate {car} could not be parked.")

    print("\nParking Lot Mapping:")
    print(parking_lot.map_to_json())


if __name__ == "__main__":
    main()

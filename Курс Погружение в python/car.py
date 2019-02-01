import csv
import os


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = str(photo_file_name)
        self.carrying = carrying

    def get_photo_file_ext(self):
        file_ext = os.path.splitext(self.photo_file_name)
        file_ext = file_ext[1]
        return file_ext


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        body_whl = body_whl.split("x")
        if len(body_whl) == 3:
            self.body_length = float(body_whl[0])
            self.body_width = float(body_whl[1])
            self.body_height = float(body_whl[2])
        else:
            self.body_whl = ""

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) == 7:
                car_type = row[0]
                brand = row[1]
                passenger_seats_count = row[2]
                photo_file_name = row[3]
                body_whl = row[4]
                carrying = row[5]
                extra = row[6]
                if car_type == 'car':
                    car = Car(car_type, brand, photo_file_name, carrying, passenger_seats_count)
                    car_list.append(car)
                elif car_type == 'truck':
                    car = Truck(car_type, brand, photo_file_name, carrying, body_whl)
                    car_list.append(car)
                elif car_type == 'spec_machine':
                    car = SpecMachine(car_type, brand, photo_file_name, carrying, extra)
                    car_list.append(car)
    return car_list

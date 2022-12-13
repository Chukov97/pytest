class Car:
    """Car class"""
    _wheels = 4
    __engine_status = "Off"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_wheels(self):
        return self._wheels

    def get_engine_status(self):
        return self.__engine_status

    def get_car_name(self):
        return f"{self.brand} {self.model}"

    def start_engine(self):
        self.__engine_status = "On"
        print(f"Engine of {self.get_car_name()} started.")

    def turn_off_engine(self):
        self.__engine_status = "Off"
        print(f"Engine of {self.get_car_name()} turned off.")


if __name__ == "__main__":
    toyota_camry = Car(brand="Toyota", model="Camry")

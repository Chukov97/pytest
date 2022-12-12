class Car:
    engine_status = 'Off'

    def __init__(self, brand, model, wheels, key):
        self.brand = brand
        self.model = model
        self.wheels = wheels
        self.key = key

    def start_engine(self, key):
        if key == self.key:
            self.engine_status = 'On'
            print(f'Engine of {self.brand} {self.model} started')

    def drive(self):
        if self.engine_status == 'On':
            print(f'Ride on {self.brand} {self.model} started')
        else:
            print('Turn on engine before drive')

    def stop_engine(self):
        if self.engine_status == 'Off':
            return None
        self.engine_status = 'Off'
        print(f'Engine of {self.brand} {self.model} stopped')


toyota_camry = Car('Toyota', 'Camry', 4, 1234)
honda_trio = Car('Honda', 'Trio', 3, 1111)

print(toyota_camry.wheels)
print(honda_trio.wheels)

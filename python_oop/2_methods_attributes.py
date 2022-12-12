class Car:
    wheels = 4

    def drive(self):
        print('Car is driving')

    def stop(self):
        print('Car is stopped')


car = Car()

print(car.wheels)
print(Car.wheels)
car.drive()
car.stop()

class Car:
    pass


class A(Car):
    pass


car = Car()
car1 = Car()
a = A()

print(car)

print(isinstance(car, Car))
print(isinstance(a, Car))
print(isinstance(a, A))

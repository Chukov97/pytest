import random

MATERIALS = {
    'wood': 15,
    'steel': 50,
    'paper': 5
}


def get_price():
    print('Got price!')
    return random.randint(200, 500)


class Cube:

    def __init__(self, h, w, d, material):
        self.h = h
        self.w = w
        self.d = d
        self.material = material

    @property
    def price(self):
        return self.w * self.d * self.h * get_price()


c = Cube(10, 10, 10, 'paper')

print(c.price)
print(c.price)
print(c.price)

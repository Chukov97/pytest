class Account:

    def __init__(self, name, balance=0):
        self.__balance = 0
        self.__owner = name

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

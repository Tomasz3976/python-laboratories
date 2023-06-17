class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    def set_pineapple_allowed(self, value):
        self._pineapple_allowed = value


pizza = Pizza(['cheese', 'tomato'])
print(pizza.pineapple_allowed)

pizza.set_pineapple_allowed(True)
print(pizza.pineapple_allowed)
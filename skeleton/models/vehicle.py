class Vehicle:
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
        self._comments = []

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        if 2 <= len(value) <= 15:
            self._make = value
        else:
            raise ValueError(Vehicle.MAKE_LEN_ERR)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if 1 <= len(value) <= 15:
            self._model = value
        else:
            raise ValueError(Vehicle.MODEL_LEN_ERR)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if 0 <= value <= 1000000:
            self._price = value
        else:
            raise ValueError(Vehicle.PRICE_ERR)

    @property
    def comments(self):
        return tuple(self._comments)

    def add_comment(self, comment):
        self._comments.append(comment)

    def get_comment(self, index):
        if index > len(self._comments)-1:
            raise ValueError("Invalid comment index.")
        return self._comments[index]

    def remove_comment(self, comment):
        if comment in self._comments:
            self._comments.remove(comment)

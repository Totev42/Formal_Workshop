from models.vehicle import Vehicle


class Motorcycle(Vehicle):
    CATEGORY_LEN_MIN = 3
    CATEGORY_LEN_MAX = 10
    CATEGORY_LEN_ERR = f'Category must be between {CATEGORY_LEN_MIN} and {CATEGORY_LEN_MAX} characters long!'

    WHEELS_COUNT = 2

    def __init__(self, make, model, price, category):
        super().__init__(make, model, price)
        self.wheels = Motorcycle.WHEELS_COUNT
        self.category = category

    def __str__(self):
        output = f"Motorcycle:\n" \
               f"Make: {self.make}\n" \
               f"Model: {self.model}\n" \
               f"Wheels: {self.wheels}\n" \
               f"Price: ${self.price:.2f}\n" \
               f"Category: {self.category}\n"
        if len(self.comments) == 0:
            output += "--NO COMMENTS--"
            return output
        else:
            for comment in self.comments:
                output += "--COMMENTS--\n"
                output += str(comment)
            output += "\n--COMMENTS--"
            return output

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if 3 <= len(value) <= 10:
            self._category = value
        else:
            raise ValueError(Motorcycle.CATEGORY_LEN_ERR)

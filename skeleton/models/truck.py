from models.vehicle import Vehicle


class Truck(Vehicle):
    WEIGHT_CAP_MIN = 1
    WEIGHT_CAP_MAX = 100
    WEIGHT_CAP_ERR = f'Weight capacity must be between {WEIGHT_CAP_MIN} and {WEIGHT_CAP_MAX}!'

    WHEELS_COUNT = 8

    def __init__(self, make, model, price, weight):
        super().__init__(make, model, price)
        self.wheels = Truck.WHEELS_COUNT
        self.weight_capacity = weight

    def __str__(self):
        output = f"Truck:\n" \
               f"Make: {self.make}\n" \
               f"Model: {self.model}\n" \
               f"Wheels: {self.wheels}\n" \
               f"Price: ${self.price:.2f}\n" \
               f"Weight Capacity: {self.weight_capacity}t\n"
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
    def weight_capacity(self):
        return self._weight_capacity

    @weight_capacity.setter
    def weight_capacity(self, value):
        if 1 <= value <= 100:
            self._weight_capacity = value
        else:
            raise ValueError(Truck.WEIGHT_CAP_ERR)

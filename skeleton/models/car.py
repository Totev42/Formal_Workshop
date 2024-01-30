from models.vehicle import Vehicle


class Car(Vehicle):
    CAR_SEATS_MIN = 1
    CAR_SEATS_MAX = 10
    CAR_SEATS_ERR = f'Seats must be between {CAR_SEATS_MIN} and {CAR_SEATS_MAX}!'

    WHEELS_COUNT = 4

    def __init__(self, make, model, price, seats):
        super().__init__(make, model, price)
        self.wheels = Car.WHEELS_COUNT
        self.seats = seats

    def __str__(self):
        output = f"Car:\n" \
               f"Make: {self.make}\n" \
               f"Model: {self.model}\n" \
               f"Wheels: {self.wheels}\n" \
               f"Price: ${self.price:.2f}\n" \
               f"Seats: {self.seats}\n"
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
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        if 1 <= value <= 10:
            self._seats = value
        else:
            raise ValueError(Car.CAR_SEATS_ERR)

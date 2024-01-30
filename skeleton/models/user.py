from models.comment import Comment
from models.constants.user_role import UserRole
from models.vehicle import Vehicle


class User:
    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'

    def __init__(self, username, firstname, lastname, password, user_role: UserRole = "Normal"):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self._user_role = user_role
        self._is_admin = True if self._user_role == UserRole.ADMIN else False
        self._vehicles: list[Vehicle] = []

    def __str__(self):
        return f"Username: {self.username}, FullName: {self.firstname} {self.lastname}, Role: {self._user_role}"

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        if 2 <= len(value) <= 20:
            for symbol in value:
                if not symbol.isalpha() and not symbol.isdigit():
                    raise ValueError('Username contains invalid symbols!')
            self._username = value
        else:
            raise ValueError('Username must be between 2 and 20 characters long!')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if 5 <= len(value) <= 30:
            for symbol in value:
                if not symbol.isalpha() and not symbol.isdigit() and symbol not in ["@", "*", "-", "_"]:
                    raise ValueError('Password contains invalid symbols!')
            self._password = value
        else:
            raise ValueError('Password must be between 5 and 30 characters long!')

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        if 2 <= len(value) <= 20:
            self._firstname = value
        else:
            raise ValueError('Firstname must be between 2 and 20 characters long!')

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        if 2 <= len(value) <= 20:
            self._lastname = value
        else:
            raise ValueError('Lastname must be between 2 and 20 characters long!')

    @property
    def user_role(self):
        return self._user_role

    @property
    def is_admin(self):
        return self._is_admin

    @property
    def vehicles(self):
        return tuple(self._vehicles)

    def get_vehicle(self, index):
        if index > len(self._vehicles)-1:
            raise ValueError(User.THE_VEHICLE_DOES_NOT_EXIT)
        found_vehicle = self._vehicles[index]
        return found_vehicle

    def add_vehicle(self, vehicle: Vehicle):
        if self.is_admin:
            raise ValueError(User.ADMIN_CANNOT_ADD_VEHICLES_ERR)
        if len(self._vehicles) == 5 and self._user_role == UserRole.NORMAL:
            raise ValueError(User.NORMAL_USER_LIMIT_REACHED_ERR)
        self._vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if vehicle in self._vehicles:
            self._vehicles.remove(vehicle)

    def add_comment(self, comment_text, vehicle: Vehicle):
        new_comment = Comment(comment_text, self.username)
        vehicle.add_comment(new_comment)

    def remove_comment(self, comment: Comment, vehicle):
        if self.username != comment.author:
            raise ValueError(User.YOU_ARE_NOT_THE_AUTHOR)
        vehicle.remove_comment(comment)

    def print_vehicles(self):
        output = f"--USER {self.username}--\n"
        if len(self._vehicles) == 0:
            output += "--NO VEHICLES--"
            return output
        counter = 1
        for vehicle in self._vehicles:
            output += f"{counter}. {str(vehicle)}\n"
            counter += 1
        return output.removesuffix("\n")

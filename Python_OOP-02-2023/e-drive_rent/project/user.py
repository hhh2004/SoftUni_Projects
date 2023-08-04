class User:
    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        if self.first_name.strip() == "":
            raise ValueError("First name cannot be empty!")

        self.last_name = last_name
        if self.last_name.strip() == "":
            raise ValueError("Last name cannot be empty!")

        self.driving_license_number = driving_license_number
        if self.driving_license_number.strip() == "":
            raise ValueError("Driving license number is required!")

        self.rating = 0.0
        if self.rating < 0:
            raise ValueError("Users rating cannot be negative!")

        self.is_blocked = False

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("Users rating cannot be negative!")
        self.__rating = value

    def increase_rating(self):
        self.rating += 0.5
        if self.rating > 10.0:
            self.rating = 10.0

    def decrease_rating(self):
        rating = self.rating - 2.0
        if rating < 0.0:
            self.rating = 0.0
            self.is_blocked = True
        else:
            self.rating = rating

    def __str__(self):
        return f"{self.first_name} {self.last_name} Driving license: {self.driving_license_number} \
Rating: {self.rating}"

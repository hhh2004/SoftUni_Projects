from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=180.0)

    def drive(self, mileage: float):
        percentage_of_max_mileage = round(100 * mileage / self.max_mileage)
        self.battery_level -= (percentage_of_max_mileage + 5)

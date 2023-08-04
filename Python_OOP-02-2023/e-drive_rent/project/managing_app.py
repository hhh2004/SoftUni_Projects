from project.user import User
from project.route import Route
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.passenger_car import PassengerCar
from project.vehicles.cargo_van import CargoVan


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        else:
            self.users.append(User(first_name, last_name, driving_license_number))
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        vehicle_types_dict = {
            "PassengerCar": PassengerCar,
            "CargoVan": CargoVan
        }

        if vehicle_type not in vehicle_types_dict.keys():
            return f"Vehicle type {vehicle_type} is inaccessible."
        else:
            for vehicle in self.vehicles:
                if vehicle.license_plate_number == license_plate_number:
                    return f"{license_plate_number} belongs to another vehicle."
            else:
                self.vehicles.append(vehicle_types_dict[vehicle_type](brand, model, license_plate_number))
                return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                else:
                    route.is_locked = True
        else:
            route_id = len(self.routes) + 1
            self.routes.append(Route(start_point, end_point, length, route_id))
            return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                break
        else:
            raise Exception("Invalid DLN!")

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                break
        else:
            raise Exception("Invalid LPN!")

        for route in self.routes:
            if route.route_id == route_id:
                break
        else:
            raise Exception("Invalid Route ID!")

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        elif vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        elif route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        else:
            vehicle.drive(route.length)
            if is_accident_happened:
                vehicle.change_status()
                user.decrease_rating()
            else:
                user.increase_rating()
            return vehicle.__str__()

    def repair_vehicles(self, count: int):
        count_of_repaired_vehicles = 0
        sorted_vehicles = sorted(self.vehicles, key=lambda x: x.model)
        sorted_vehicles = sorted(sorted_vehicles, key=lambda x: x.brand)

        for vehicle in sorted_vehicles:
            if count <= 0:
                break
            if vehicle.is_damaged:
                vehicle.change_status()
                vehicle.recharge()
                count_of_repaired_vehicles += 1
                count -= 1

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: x.rating, reverse=True)
        output = ["*** E-Drive-Rent ***"]

        for user in sorted_users:
            output.append(user.__str__())

        output = "\n".join(output)
        return output

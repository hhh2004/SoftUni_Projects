class Route:
    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point = start_point
        if start_point.strip() == '':
            raise ValueError("Start point cannot be empty!")

        self.end_point = end_point
        if end_point.strip() == '':
            raise ValueError("End point cannot be empty!")

        self.length = length
        if length < 1.0:
            raise ValueError("Length cannot be less than 1.00 kilometer!")

        self.route_id = route_id
        self.is_locked = False

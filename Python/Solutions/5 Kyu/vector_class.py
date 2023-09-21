class Vector:
    def __init__(self, coordinates: list):
        self.coordinates = coordinates
        self.dimensions = len(coordinates)
        self.dimension_error = (
            "Supplied vector doesn't have the same dimensions as the current vector!"
        )

    def __str__(self):
        return "(" + ",".join(str(x) for x in self.coordinates) + ")"

    def __repr__(self):
        return str(self)

    def add(self, other):
        if other.dimensions == self.dimensions:
            return Vector([x + y for x, y in zip(self.coordinates, other.coordinates)])
        else:
            raise ValueError(self.dimension_error)

    def subtract(self, other):
        if other.dimensions == self.dimensions:
            return Vector([x - y for x, y in zip(self.coordinates, other.coordinates)])
        else:
            raise ValueError(self.dimension_error)

    def dot(self, other):
        if other.dimensions == self.dimensions:
            return sum(x * y for x, y in zip(self.coordinates, other.coordinates))
        else:
            raise ValueError(self.dimension_error)

    def norm(self) -> float:
        return sum(x**2 for x in self.coordinates) ** 0.5

    def equals(self, other) -> bool:
        return self.coordinates == other.coordinates

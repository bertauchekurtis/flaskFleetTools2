# plane.py
import logging
log = logging.getLogger("plane")

class Plane:
    def __init__(self, 
                 model: str, 
                 family: str,
                 capacity: int,
                 category: str,
                 turnaround: int,
                 runwayRequirement: int,
                 maxFlyingRange: int,
                 fuelBurn: int,
                 speed: int,
                 maxLifespan: int,
                 manufacturer: str,
                 price: int):
        self.model = model
        self.family = family
        self.capacity = capacity
        self.category = category
        self.turnaround = turnaround
        self.runwayRequirement = runwayRequirement
        self.maxFlyingRange = maxFlyingRange
        self.fuelBurn = fuelBurn
        self.speed = speed
        self.maxLifespan = maxLifespan
        self.manufacturer = manufacturer
        self.price = price

    # TODO:
    # make this type hashable

    
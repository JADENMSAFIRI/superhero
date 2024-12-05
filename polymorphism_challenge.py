# Base class for vehicles
class Vehicle:
    def move(self):
        """
        Generic move method for a vehicle.
        """
        print("The vehicle is moving.")

# Subclass for Car
class Car(Vehicle):
    def move(self):
        """
        Define how a car moves.
        """
        print("Driving 🚗...")

# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        """
        Define how a plane moves.
        """
        print("Flying ✈️...")

# Subclass for Boat
class Boat(Vehicle):
    def move(self):
        """
        Define how a boat moves.
        """
        print("Sailing 🚤...")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

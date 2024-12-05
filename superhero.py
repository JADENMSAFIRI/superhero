# Base Superhero class
class Superhero:
    def __init__(self, name, power, weakness):
        """
        Initialize the superhero with unique attributes.
        """
        self.name = name
        self.power = power
        self.weakness = weakness

    def display_info(self):
        """
        Display basic information about the superhero.
        """
        return f"Name: {self.name}, Power: {self.power}, Weakness: {self.weakness}"

    def use_power(self):
        """
        Simulate using a superhero's power.
        """
        print(f"{self.name} is using their power: {self.power}!")


# Subclass for a specific type of superhero (e.g., TechHero)
class TechHero(Superhero):
    def __init__(self, name, power, weakness, gadget):
        """
        Add an additional attribute for the hero's gadget.
        """
        super().__init__(name, power, weakness)
        self.gadget = gadget

    def use_power(self):
        """
        Override use_power to include the gadget.
        """
        print(f"{self.name} uses {self.gadget} to unleash their power: {self.power}!")


# Example usage
hero1 = Superhero("Captain Strong", "Super Strength", "Kryptonite")
print(hero1.display_info())
hero1.use_power()

hero2 = TechHero("Iron Genius", "Intelligence", "Overheating", "Advanced Suit")
print(hero2.display_info())
hero2.use_power()

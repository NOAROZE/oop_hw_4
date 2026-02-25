class SpaceShip:
    MAX_FUEL = 1000
    MIN_FUEL = 0
    launch_count = 0
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
    @property
    def fuel(self):
        return self.__fuel
    @fuel.setter
    def fuel(self, value):
        if value > SpaceShip.MAX_FUEL:
            self.__fuel = SpaceShip.MAX_FUEL
        elif value < SpaceShip.MIN_FUEL:
            self.__fuel = SpaceShip.MIN_FUEL
        else:
            self.__fuel = value
    @staticmethod
    def is_valid_mission(dist):
        return 50 < dist < 10000
    @classmethod
    def from_emergency_mode(cls, name):
        return cls(name, 100)

    def launch(self):
        if self.fuel < 100:
            print("Not enough fuel to launch")
        else:
            self.fuel -= 100
            SpaceShip.launch_count += 1
            print(f"{self.name} has launched!")

    def refuel(self, amount):
        self.fuel = self.fuel + amount

    def display_status(self):
        print(f"Ship: {self.name} | Fuel: {self.fuel} | Total Launches: {SpaceShip.launch_count}")



ship1 = SpaceShip("noa", 100)
ship1.display_status()
ship2 = SpaceShip("israel", 1100)
ship2.display_status()
ship3 = SpaceShip.from_emergency_mode("naama")
ship3.display_status()
print(ship1.launch())
print(ship2.launch())
print(ship3.launch())
ship1.display_status()
ship2.display_status()
ship3.display_status()
ship1.refuel(50)
ship2.refuel(200)
ship3.refuel(-50)
ship1.display_status()
ship2.display_status()
ship3.display_status()
dist1 = SpaceShip.is_valid_mission(0)
print(dist1)
dist2 = SpaceShip.is_valid_mission(100)
print(dist2)






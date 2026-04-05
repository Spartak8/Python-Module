class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = float(height)
        self._age = age

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {int(self._height)}cm")

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self):
        self._bloomed = True


class Tree(Plant):
    def __init__(self, name, height, age, diameter):
        super().__init__(name, height, age)
        self.diameter = float(diameter)

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.diameter}cm")

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.diameter}cm wide")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self):
        self._height = round(self._height + 2.1, 1)

    def age(self):
        self._age += 1
        self.nutritional_value += 1

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def main():
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()
    print()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print()
    print()
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April")
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    for day in range(20):
        vegetable.grow()
        vegetable.age()
    vegetable.show()


if __name__ == "__main__":
    main()

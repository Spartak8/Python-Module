class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = float(height)
        self._age = age
        self._stats = Plant.Stats()

    def show(self) -> None:
        self._stats._show_count += 1
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self, growth_rate: float = 1.0) -> None:
        self._stats._grow_count += 1
        self._height = round(self._height + growth_rate, 1)

    def age(self, days: int = 1) -> None:
        self._stats._age_count += 1
        self._age = self._age + days

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")
            print(f" {self._shade_count} shade")

    def __init__(self, name: str, height: float,
                 age: int, diameter: float) -> None:
        super().__init__(name, height, age)
        self.diameter = float(diameter)
        self._stats = Tree.Stats()
        self._stats: Tree.Stats = Tree.Stats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.diameter}cm")

    def produce_shade(self) -> None:
        self._stats._shade_count += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.diameter}cm wide.")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True

    def grow(self, growth_rate: float = 8.0) -> None:
        super().grow(growth_rate)


class Seed(Flower):
    def __init__(self, name: str,
                 height: float, age: int, color: str, seeds: int = 0) -> None:
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def grow(self, growth_rate: float = 30.0) -> None:
        super().grow(growth_rate)

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def bloom(self, seeds: int = 0) -> None:
        super().bloom()
        self._seeds = seeds


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom(42)
    sunflower.show()
    display_stats(sunflower)

    print("\n=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    display_stats(anon)


if __name__ == "__main__":
    main()

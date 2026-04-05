class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.days += 1


def main() -> None:
    plant = Plant("Rose", 25.0, 30)
    s_height = plant.height

    print("=== Garden Plant Growth ===")
    plant.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()

    total = round(plant.height - s_height, 1)

    print(f"Growth this week: {total}cm")


if __name__ == "__main__":
    main()

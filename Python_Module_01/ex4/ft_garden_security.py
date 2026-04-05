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


def main():
    plant = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    plant.show()
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    plant.set_age(-10)
    print()
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()

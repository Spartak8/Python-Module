class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error() -> None:
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as w:
        print(f"Caught WaterError: {w}")


def test_garden_error() -> None:
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as w:
        print(f"Caught GardenError: {w}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    test_plant_error()
    print()
    test_water_error()
    print()
    test_garden_error()
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
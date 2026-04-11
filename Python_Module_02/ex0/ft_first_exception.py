def input_temperature(temp_str: str) -> int | None:
    try:
        return int(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return None


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")
    x = input_temperature("25")
    print(f"Temperature is now {x}°C")
    print()
    print("Input data is 'abc'")
    input_temperature("abc")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print("Input data is '25'")
    x = input_temperature("25")
    print(f"Temperature is now {x}°C")
    print()
    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()
    print("Input data is '100'")
    try:
        input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()
    print("Input data is '-50'")
    try:
        input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
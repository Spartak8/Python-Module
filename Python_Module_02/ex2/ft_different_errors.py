def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")        
    elif operation_number == 1:
        i = 10 / 0
    elif operation_number == 2:
        open("khj")
    elif operation_number == 3:
        x = "abc" + 10
    elif operation_number == 4:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as z:
        print(f"Caught ZeroDivisionError: {z}")
    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as f:
        print(f"Caught FileNotFoundError: {f}")
    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as t:
        print(f"Caught TypeError: {t}")
    print("Testing operation 4...")
    garden_operations(4)
    print("Operation completed successfully")
    print()
    print("All error types tested successfully!")
    

if __name__ == "__main__":
    test_error_types()
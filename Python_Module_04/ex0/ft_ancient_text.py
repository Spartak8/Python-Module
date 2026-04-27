import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
else:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file = open(f"{sys.argv[1]}", "r")
        text = file.read()
        file.close()
        print("---")
        print(f"{text}")
        print("---")
        print(f"File '{sys.argv[1]}' closed.")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")

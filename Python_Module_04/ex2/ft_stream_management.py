import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
else:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file = open(f"{sys.argv[1]}", "r")
        text = file.read()
        file.close()
        print("---")
        print()
        print(f"{text}")
        print()
        print("---")
        print(f"File '{sys.argv[1]}' closed.")
        print()
        print("Transform data:")
        lines = text.splitlines()
        new = []
        for line in lines:
            new.append(line + "#")
        print("---")
        print()
        for line in new:
            print(line)
        print()
        print("---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        name = sys.stdin.readline().strip()                    
        if not name:
            print("Not saving data.")
        else:
            try:
                print(f"Saving data to '{name}'")
                file = open(name, "w")
                file.write("\n".join(new))
                file.close()
                print(f"Data saved in file '{name}'.")
            except Exception as e:
                sys.stderr.write(f"[STDERR] Error opening file '{name}': {e}\n")
                print("Data not saved.")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
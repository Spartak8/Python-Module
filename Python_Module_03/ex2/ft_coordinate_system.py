import math


def get_player_pos() -> tuple:
    while True:
        cord = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            x_str, y_str, z_str = cord.split(",")
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x_f = float(x_str.strip())
        except ValueError as e:
            print(f"Error on parameter '{x_str.strip()}': {e}")
            continue

        try:
            y_f = float(y_str.strip())
        except ValueError as e:
            print(f"Error on parameter '{y_str.strip()}': {e}")
            continue

        try:
            z_f = float(z_str.strip())
        except ValueError as e:
            print(f"Error on parameter '{z_str.strip()}': {e}")
            continue

        return (x_f, y_f, z_f)


print("=== Game Coordinate System ===")
print()
print("Get a first set of coordinates")
pos1 = get_player_pos()
print(f"Got a first tuple: {pos1}")
print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
dist = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
print(f"Distance to center: {dist:.4f}")
print()
print("Get a second set of coordinates")
pos2 = get_player_pos()
dist2 = math.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2 +
                  (pos2[2]-pos1[2])**2)
print(f"Distance between the 2 sets of coordinates: {dist2:.4f}")

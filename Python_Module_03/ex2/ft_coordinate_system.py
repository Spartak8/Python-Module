import math


def get_player_pos():
    while True:
        cord = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            x_str, y_str, z_str = cord.split(",")
            x_f = float(x_str.strip())
            y_f = float(y_str.strip())
            z_f = float(z_str.strip())
            return (x_f, y_f, z_f)
        except ValueError:
            print("Invalid syntax")


print("=== Game Coordinate System")
print("Get a first set of coordinates")
pos = get_player_pos()
print(f"Got a first tuple: {pos}")
print(f"It includes: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")

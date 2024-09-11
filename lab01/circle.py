import math
radius = input("Enter the radius of a circle ")

radiusFloat = float(radius)

perimeter = 2 * math.pi * radiusFloat
area = math.pi * radiusFloat ** 2

print(f"The circle with radius {radius} has an area of {area:.2f} and a perimeter of {perimeter:.2f}")

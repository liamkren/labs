
InCm = 2.54
YdM = 0.9144
OzG = 28.349523125
lbsKg = 0.45359237

entry = input("input a distance or weight amount with a space and unit after( in, cm, yd, m, oz, g, kg, lb)")

numberString, unit = entry.split()
number = float(numberString)

if unit == "cm":
    convertedNum = number / InCm
    convertedUnit = "in" 
elif unit == "in":
    convertedNum = number * InCm
    convertedUnit = "cm"
elif unit == "m":
    convertedNum = number / YdM
    convertedUnit = "yd"
elif unit == "yd":
    convertedNum = number * YdM
    convertedUnit = "m"
elif unit == "oz":
    convertedNum = number * OzG
    convertedUnit = "g"
elif unit == "g":
    convertedNum = number / OzG
    convertedUnit = "oz"
elif unit == "lb":
    convertedNum = number * lbsKg
    convertedUnit = "kg"
elif unit == "kg":
    convertedNum = number / lbsKg
    convertedUnit = "lb"

print(f"{number} {unit} = {convertedNum:.2f} {convertedUnit}")
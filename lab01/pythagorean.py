import math

sidea = input("Enter the length of the first side  ")
sideb = input("Enter the length of the second side  ")
    
a = float(sidea)
b = float(sideb)

sidec = math.sqrt(a ** 2 + b ** 2)
    
  
print(f"The hypotenuse is {sidec:.2f}")
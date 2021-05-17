
weight = int(input('Weight: '))
unit = input('(L)bs (K)g ')
if unit.upper() == "L":
   converted = weight * 0.48
   print(f"You are {converted}")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

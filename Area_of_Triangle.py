#Area of Triangle
first_side = float(input("Enter measurement of first side: "))
second_side = float(input("Enter measurement of second side: "))
third_side = float(input("Enter measurement of third side: "))

#semiparameter
s = (first_side + second_side + third_side) / 2

#area
area = (s*(s-first_side)*(s-second_side)*(s-third_side))**0.5
print("Area of triangle is %0.3f" %area)
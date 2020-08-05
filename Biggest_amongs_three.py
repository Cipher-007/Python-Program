#Find largest no amongs three
num1 = float(input("Enter first no: "))
num2 = float(input("Enter second no: "))
num3 = float(input("Enter three no: "))

if (num1>num2) and (num1>num3):
    print(f"{num1} is the largest no ")
elif (num2>num1) and (num2>num3):
    print(f"{num2} is the largest no ")
else:
    print(f"{num3} is the largest no ")
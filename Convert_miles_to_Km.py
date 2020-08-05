#Converting Miles to Kilometers
miles = float(input("Enter Miles to be converted into Kilometers: "))

#Conversion factor
conversion_factor = 1.609

#Conversion
kilometers = miles * conversion_factor
print(f"{miles}mi is {kilometers}Km")
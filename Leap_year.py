#Check if entered year is leap or not
leap_year = int(input("Enter year to be checked: "))

if (leap_year % 4) == 0:
    if (leap_year % 100) == 0:
        if (leap_year % 400) == 0:
            print(f"{leap_year} is a leap year ")
        else :
            print(f"{leap_year} is not a leap year ")
    else :
        print(f"{leap_year} is a leap year ")
else :
    print(f"{leap_year} is not a leap year ")
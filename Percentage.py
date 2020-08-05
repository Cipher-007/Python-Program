#Calculate Percentage of total marks

subject1 = float(input("Marks of Subject 1: "))
subject2 = float(input("Marks of Subject 2: "))
subject3 = float(input("Marks of Subject 3: "))
subject4 = float(input("Marks of Subject 4: "))

total_marks = subject1 + subject2 + subject3 + subject4

percentage = (total_marks / 400)*10

if percentage <= 10.0 and percentage >= 7.75:
    print(f"First class with Distinction with {percentage}")
elif percentage < 7.75 and percentage >= 6.0:
    print(f"First class with {percentage}")
elif percentage < 6.0 and percentage >= 5.0:
    print(f"Second class with {percentage}")
elif percentage < 5.0 and percentage >= 3.5:
    print(f"Third class with {percentage}")
else:
    print(f"Fail with {percentage}")
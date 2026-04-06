###36Task 1: Variables and Data Types Create variables to store a person's name (string), age (integer), height in meters (float), and whether they are a student (boolean). Print all four values in a single print() statement.
Name="krishna"
Age=35
height=5.5
Student=True
print("Name",Name,"Age",Age,"height",height,"Student",Student)
#Task 2: String Formatting Using the variables from Task 1, print a sentence in the following format:
print(f"Name:{Name}|Age:{Age}|height{height}|Student:{Student}")
#########Task 3: Arithmetic Operations Using the age variable, calculate and print:
Age=int(input("Provide age"))
Age_months=Age*12
Age_days=Age*365
Remainder=Age%7
power=Age**2
print("Age_months",Age_months,"Age_days",Age_days,"Remainder",Remainder,"power",power)


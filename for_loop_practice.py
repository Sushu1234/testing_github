#Task 1 Write a for loop that prints all numbers from 1 to 5 using range()

for i in range(1,6):
    print(i)
print("end of task1")   

#Task 2 Write a for loop that prints only odd numbers between 1 and 10 using the step parameter in range().
print("#####task2 output########")
for i in range(1,6,1):
    odd=(2*i)-1
    print(odd)
print("end of task2")

#Task 3 Write a nested for loop that prints the following pattern:
#output
#0 0
#0 1
#1 0
#1 1
#2 0
#2 1
print("#####task3 output########")
for i in range(3):
    for j in range(2):
        print(i,j)
#Task 4 Write a for loop that prints numbers from 1 to 7. If the number is 5, stop the loop immediately using break.
# # Use range(1, 8) to include numbers from 1 to 7
# for number in range(1, 8):
#     if number == 5:
#         break  # Immediately exits the loop when number is 5
#     print(number)




print("#####task4 output########")
for i in range(1,8):
    if(i!=5):
        print(i)
    else:
        break




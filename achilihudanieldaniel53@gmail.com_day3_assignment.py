# # Python Beginner Assignment
# # Topics Covered: Data Types, Operators, Conditional Statements, and Loops



# # 1. Even or Odd
# # Write a program to take an integer as input and print whether it is Even or Odd.

number = (int(input("Enter any given number of your choice: ")))
print (number)

if number % 2 == 0:
    print (f"The number '{number}' inputed is an Even Number!")
else:
    print (f"The number '{number}' inputed is an Odd Number!")
    



# # 2. Multiplication Table
# # Write a program to print the multiplication table of a given number up to 10. Example: Input 7 -> # print 7 x 1 = 7 ... 7 x 10 = 70.

random_number = (float(input("Enter any given number of your choice: ")))
random_number_mul_table = [f"{random_number} x {b} = {random_number * b}" for b in range(1,11)]


print(f"The multiplication table of '{random_number}' up to 10 is: ")
print("\n".join(random_number_mul_table))




# # 3. Sum of Natural Numbers
# # Write a program to take a positive integer n and find the sum of the first n natural numbers using a loop. Example: Input 5 -> Output 15.

postive_integer =  (int(input("Enter any given positive number of your choice: ")))

if postive_integer > 0 :
    total_sum_of_positive_integer = 0

    for i in range (1, postive_integer +1):
        total_sum_of_positive_integer += i

    print (f" The sum of the first n natural numbers of '{postive_integer}' is: ")
    print (total_sum_of_positive_integer)
else:
    print ("Enter a positive integer")




# # 4. Count Digits
# # # Write a program to take an integer as input and count the total number of digits in it. Example: Input 45892 -> Output 5.

random_integer = (int(input("Enter any given number of your choice: ")))
random_integer_count = len(str(abs(random_integer)))

print (f"The total number of digits in '{random_integer}' is '{random_integer_count}'")




# # 5. Simple Calculator
# # Write a program that takes two numbers and an operator (+, -, *, /) from the user and performs the corresponding operation using if-elif-else. Handle division by zero appropriately.


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")


if operator == '+':
    result = number1 + number2
    print(f"Result: {number1} + {number2} = {result}")

elif operator == '-':
    result = number1 - number2
    print(f"Result: {number1} - {number2} = {result}")

elif operator == '*':
    result = number1 * number2
    print(f"Result: {number1} * {number2} = {result}")

elif operator == '/':
    if number2 != 0:
        result = number1 / number2
        print(f"Result: {number1} / {number2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Error: Invalid Operator Entered. Please Use +, -, *, or /.")

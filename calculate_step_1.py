
from calculate_sum import calculate_sum

operation = input("Enter an operation: ")
first_number = int(input("Enter a number: "))
second_number = int(input("Enter a number: "))

print("The answer is " + str(calculate_sum(operation, first_number, second_number)))